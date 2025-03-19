def count_points_in_rectangle(x1, y1, x2, y2):
            return (
                prefix_sum[x2+1][y2 +1] - prefix_sum[x2+1][y1] - prefix_sum[x1][y2 + 1] + prefix_sum[x1][y1]
            )
        
        original_points = list(zip(xCoord, yCoord))
        if len(original_points) < 4:
            return -1

        unique_x_coords = sorted(set(xCoord))
        unique_y_coords = sorted(set(yCoord))

        x_to_compressed = {x:i for i, x in enumerate(unique_x_coords)}
        y_to_compressed = {y:i for i, y in enumerate(unique_y_coords)}

        compressed_points = [(x_to_compressed[x], y_to_compressed[y]) for x, y in original_points]
        num_unique_x = len(unique_x_coords)
        num_unique_y = len(unique_y_coords)

        occupancy_grid = [[0] * (num_unique_y + 1) for _ in range(num_unique_x + 1)]
        for cx, cy in compressed_points:
            occupancy_grid[cx][cy]  = 1

        prefix_sum = [[0 for _ in range(num_unique_y+1)] for _ in range(num_unique_x+1)]

        
        for i in range(1, num_unique_x + 1):
            for j in range(1, num_unique_y+1):
                prefix_sum[i][j] = (
                    occupancy_grid[i-1][j-1]+prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
                )
        
        points_by_x = defaultdict(list)
        for x, y in original_points:
            points_by_x[x].append(y)

        for x in points_by_x:
            points_by_x[x].sort()

        sorted_x_keys = sorted(points_by_x.keys())
        max_area = -1
        num_unique_sorted_x = len(sorted_x_keys)

        for i in range(num_unique_sorted_x):
            for j in range(i + 1, num_unique_sorted_x):
                x_left = sorted_x_keys[i]
                x_right = sorted_x_keys[j]

                x_values_left = set(points_by_x[x_left])
                y_values_right = set(points_by_x[x_right])

                common_y_values = sorted(x_values_left.intersection(y_values_right))

                for a in range(len(common_y_values) - 1):
                    for b in range(a+1, len(common_y_values)):
                        y_bottom = common_y_values[a]
                        y_top = common_y_values[b]

                        X_left_idx = x_to_compressed[x_left]
                        X_right_idx = x_to_compressed[x_right]
                        Y_bottom_idx = y_to_compressed[y_bottom]
                        Y_top_idx = y_to_compressed[y_top]

                        points_inside = count_points_in_rectangle(
                            min(X_left_idx, X_right_idx),
                            min(Y_bottom_idx, Y_top_idx),
                            max(X_left_idx, X_right_idx),
                            max(Y_bottom_idx, Y_top_idx)
                        )

                        if points_inside == 4:
                            area = (x_right - x_left) * (y_top - y_bottom)
                            max_area = max(max_area, area)
        return max_area
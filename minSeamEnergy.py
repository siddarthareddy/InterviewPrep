def minSeamEnergy(pixel_energies):
    previous_seam_energies_row = list(pixel_energies[0])
    # Skip the first row in the following loop.
    for y in range(1, len(pixel_energies)):
        pixel_energies_row = pixel_energies[y]

        seam_energies_row = []
        for x, pixel_energy in enumerate(pixel_energies_row):
            # Determine the range of x values to iterate over in the previous
            # row. The range depends on if the current pixel is in the middle of
            # the image, or on one of the edges.
            x_left = max(x - 1, 0)
            x_right = min(x + 1, len(pixel_energies_row) - 1)
            x_range = range(x_left, x_right + 1)

            min_seam_energy = pixel_energy + \
                              min(previous_seam_energies_row[x_i] for x_i in x_range)
            seam_energies_row.append(min_seam_energy)

        previous_seam_energies_row = seam_energies_row
    return min(seam_energy for seam_energy in previous_seam_energies_row)

ENERGIES = [
    [9, 9, 0, 9, 9],
    [9, 1, 9, 8, 9],
    [9, 9, 9, 9, 0],
    [9, 9, 9, 0, 9],
]

print(minSeamEnergy(ENERGIES))
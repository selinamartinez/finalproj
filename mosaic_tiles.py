import glob
from PIL import Image
from scipy import spatial
import numpy as np
import matplotlib.pyplot as plt

def createPhotomosaic(photo):

    #photo that will become a photo mosaic
    main_photo_path = photo

    #tiles that create the photomosaic
    tile_photos_path = "tiles/*"
    tile_size = (50, 50)

    #Getting all the tiles
    tile_paths = []
    for file in glob.glob(tile_photos_path):
        tile_paths.append(file)

    tiles = []
    for path in tile_paths:
        tile = Image.open(path)
        tile = tile.resize(tile_size)
        tiles.append(tile)

    #Calculate dominant color 
    colors = []
    for tile in tiles:
        dom_color = np.array(tile).mean(axis=0).mean(axis=0)
        colors.append(dom_color)


    #Pixelate main photo
    main_photo = Image.open(main_photo_path)
    width = int(np.round(main_photo.size[0] / tile_size[0]))
    height = int(np.round(main_photo.size[1] / tile_size[1]))

    resized_photo = main_photo.resize((width, height))

    # Create a KDTree
    tree = spatial.KDTree(colors)

    # Empty integer array to store indices of tiles
    closest_tiles = np.zeros((width, height), dtype=np.uint32)

    for i in range(width):
        for j in range(height):
            pixel = resized_photo.getpixel((i,j))
            closest = tree.query(pixel)
            closest_tiles[i,j] = closest[1] 

    # Create an output image
    output = Image.new('RGB', main_photo.size)

    # Draw tiles
    for i in range(width):
        for j in range(height):
            # Offset of tile
            x, y = i*tile_size[0], j*tile_size[1]
            # Index of tile
            index = closest_tiles[i, j]
            # Draw tile
            output.paste(tiles[index], (x, y))

    # Save output
    output.save("output_image.jpg")
    plt.figure()
    plt.imshow("output_image.jpg") 
    plt.show()  # display it
    
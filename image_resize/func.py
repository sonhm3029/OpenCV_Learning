import matplotlib.pyplot as plt
import math

# def display1(image, resize_down_img, resize_up_img):
#     fig = plt.figure(figsize=(60, 60))
#     plt.rcParams['axes.titlesize'] = 60
#     ax1 = plt.subplot(1, 3, 1)
#     ax2 = plt.subplot(1, 3, 2)
#     ax3 = plt.subplot(1, 3, 3)

#     ax1.set_title("Original")
#     ax2.set_title("Resize down")
#     ax3.set_title("Resize up")

#     fig.add_subplot(ax1)
#     plt.imshow(image)
#     fig.add_subplot(ax2)
#     plt.imshow(resize_down_img)
#     fig.add_subplot(ax3)
#     plt.imshow(resize_up_img)


#     plt.show()
    
def plot_images(img_dict, num_cols):
    img_arr = img_dict['list_img']
    num_img = len(img_arr)
    print(num_img)
    img_label = img_dict['list_label']
    # plt.rcParams[''] = 60
    plt.rcParams['axes.titlesize'] = 24
    plt.rcParams['figure.figsize'] = (50, 50)
    num_rows = math.ceil(num_img / num_cols)
    # subplot_arr = []
    flag = 0
    print(f"num rows: {num_rows}")
    for i, image in enumerate(img_arr):
        print(i)
        plt.subplot(num_rows, num_cols, i+1)
        plt.title(img_label[i])
        plt.imshow(img_arr[i])
    
    plt.show()
    
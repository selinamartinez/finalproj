image = imread('image.jpg');

im1 = image(:,:,1);
edgeDetector = [1 1 1; 0 0 0; -1 -1 -1]; % edge detection kernel

processed_1 = conv2(im1, edgeDetector, 'same');

binaryImage = processed_1 > 128;

figure(1)
binaryImage = imclearborder(binaryImage);
boundaries = bwboundaries(binaryImage);
x = boundaries{1}(:, 2);
y = boundaries{1}(:, 1);
hold on;
plot(x, y, 'r-', 'LineWidth', 2);
hold off;

%% Image Processing
edgeDetector = [1 1 1; 0 0 0; -1 -1 -1]; % edge detection kernel

image = imread('image.jpg');

figure(2)

% ORIGINAL IMAGES
image_1 = image(:,:,1);
subplot(3,2,1)
imshow(image_1) % image 1, light greyscale
title('Original image 1')

image_2 = image(:,:,2);
subplot(3,2,3)
imshow(image_2) % image 2, medium greyscale
title('Original image 2')

image_3 = image(:,:,3);
subplot(3,2,5)
imshow(image_3) % image 3, dark greyscale 
title('Original image 3')

% PROCESSED IMAGES
processed_1 = conv2(image_1, edgeDetector, 'same');
subplot(3, 2, 2)
imshow(processed_1) % edge detector 1
title('Processed image 1')

processed_2 = conv2(image_2, edgeDetector, 'same');
subplot(3, 2, 4)
imshow(processed_2) % edge detector 2
title('Processed image 2')

processed_3 = conv2(image_3, edgeDetector, 'same');
subplot(3, 2, 6)
imshow(processed_3) % edge detector 3
title('Processed image 3')


set(gcf,'Position',[200 200 1000 500])
sgtitle('3.4 Image Processing')

% The darker the greyscale, the more noise in the edge detection processed
% image



%% Image Processing Using Sobel Edge Detection
 
figure(3)
% AVERAGED IMAGES 
avg_filter = [1 2 1; 2 4 2; 1 2 1]./16; % --> Adding averaging filter to images reduces noise in edge detection
avg_1 = conv2(image_1, avg_filter, 'same');
subplot(3,5,1)
imshow(avg_1) % averaged image 1
title('Averaged image 1')
 
avg_2 = conv2(image_2, avg_filter, 'same');
subplot(3,5,6)
imshow(avg_2) % averaged image 2
title('Averaged image 2')
 
avg_3 = conv2(image_3, avg_filter, 'same');
subplot(3,5,11)
imshow(avg_3) % averaged image 3
title('Averaged image 3')
 
% X-PROCESSED IMAGES
X_kernel = [-1 0 1; -2 0 2; -1 0 1]; % X edge detection kernel
 
X_1 = conv2(avg_1, X_kernel, 'same');
subplot(3, 5, 2)
imshow(X_1) % X-detector 1
title('X-Processed image 1')
 
X_2 = conv2(avg_2, X_kernel, 'same');
subplot(3, 5, 7)
imshow(X_2) % X-detector 2
title('X-Processed image 2')
 
X_3 = conv2(avg_3, X_kernel, 'same');
subplot(3, 5, 12)
imshow(X_3) % X-detector 3
title('X-Processed image 3')
 
% Y-PROCESSED IMAGES
Y_kernel = [-1 -2 -1; 0 0 0; 1 2 1]; % Y edge detection kernel
 
Y_1 = conv2(avg_1, Y_kernel, 'same');
subplot(3, 5, 3)
imshow(Y_1) % X-detector 1
title('Y-Processed image 1')
 
Y_2 = conv2(avg_2, Y_kernel, 'same');
subplot(3, 5, 8)
imshow(Y_2) % X-detector 2
title('Y-Processed image 2')
 
Y_3 = conv2(avg_3, Y_kernel, 'same');
subplot(3, 5, 13)
imshow(Y_3) % X-detector 3
title('Y-Processed image 3')
 
% X + Y
XY_1 = X_1 + Y_1;
subplot(3, 5, 4)
imshow(XY_1) % X+Y Sobel Edge Detector 1
title('Sobel image 1')
 
XY_2 = X_2 + Y_2;
subplot(3, 5, 9)
imshow(XY_2) % X+Y Sobel Edge Detector 2
title('Sobel image 2')
 
XY_3 = X_3 + Y_3;
subplot(3, 5, 14)
imshow(XY_3) % X+Y Sobel Edge Detector 3
title('Sobel image 3')
 
% ORIGINAL IMAGES
subplot(3,5,5)
imshow(image_1) % image 1, light grey scale
title('Original image 1')
 
subplot(3,5,10)
imshow(image_2) % image 2, medium grey scale
title('Original image 2')
 
subplot(3,5,15)
imshow(image_3) % image 3, dark grey scale 
title('Original image 3')
 
 
set(gcf,'Position',[200 200 1000 500])
sgtitle('Image Processing Sobel Edge Detection Method')
from __future__ import division

import matlab.engine


I = im2double(imread('/home/cocoslabs/Downloads/download (2).jpeg'));
figure(1); imshow(I); title('Source image');

PSF = fspecial('motion', 14, 0);
noise_mean = 0;
noise_var = 0.0001;
estimated_nsr = noise_var / var(I);

I = edgetaper(I, PSF);
figure(2); imshow(deconvwnr(I, PSF, estimated_nsr)); title('Result');
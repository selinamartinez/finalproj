topN = 50;
img = imread('image.jpg');
rimg = reshape(img, [], 3);
[urgb, ~, uidx] = unique(rimg, 'rows');
labs = reshape(uint32(uidx),size(img,1),size(img,2));
recolored = uint8(ind2rgb(labs-1, urgb));
subplot(2,2,1)
image(img);
title('original')
counts = accumarray(uidx,1);
[sortedcounts, sortidx] = sort(counts,'descend');
mcc1 = urgb(sortidx(1),:);
mcc2 = urgb(sortidx(2),:);
subplot(2,2,3)
image(reshape(mcc1,1,1,3))
title(sprintf('Most common color [%d,%d,%d]\n%d occurrences', mcc1, sortedcounts(1)));
subplot(2,2,4)
image(reshape(mcc2,1,1,3))
title(sprintf('Second most common color [%d,%d,%d]\n%d occurrences', mcc2, sortedcounts(2)));
onlytop = double(ismember(labs,sortidx(1:topN)));
subplot(2,2,2)
image(recolored, 'alphadata', onlytop);
title(sprintf('showing only top %d colors', topN));
set(gca, 'color', 'k')
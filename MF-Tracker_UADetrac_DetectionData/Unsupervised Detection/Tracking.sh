mkdir /home/gab/Downloads/ResUAdetrac

filter='300 500 900 1000 1200 1500 2000'
video='MVI_39801 MVI_40201 MVI_40213 MVI_40752 MVI_40981 MVI_63553 MVI_39861 MVI_40204 MVI_40241 MVI_40871 MVI_41063 MVI_63554 MVI_40191 MVI_40211 MVI_40243 MVI_40962 MVI_41073 MVI_63561 MVI_40192 MVI_40212 MVI_40244 MVI_40963 MVI_63552'
cd ~/code/mkcf_v2/build

for vid in $video
do
	echo $ftr
	for ftr in $filter
	do
		echo $vid
		mkdir "/home/gab/Downloads/ResUAdetrac/${vid}-mkcfv2"
		./MKCF "/home/gab/Downloads/DETRAC-train-data/Insight-MVT_Annotation_Train/${vid}/" "/media/sf_Google_Drive/uadetrac-bgs/${vid}/With mask/PAWCS/" res.xml 1000 $ftr
		mv res.xml "/home/gab/Downloads/ResUAdetrac/${vid}-mkcfv2/1000${ftr}.xml"
	done 
done 



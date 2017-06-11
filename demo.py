from flickrDownload import *

# print "Please enter a photo id:",
# photoId = raw_input()
# print "Fetching Photo"

# photoSizes = FlickrPhotosGetSizes(photo_id = photoId)
# if(photoSizes.makeCall()):
# 	print "API Call Success! Writing Photos to Disk"
# 	photoSizes.writePhotos()
# else:
# 	print "API Call Failed"


print "Fetching All Photos"

photoIds = FlickrPeopleGetPhotos(user_id = "me")
if(photoIds.makeCall()):
	print "API Call Success! Downloading photo by ID"
	# for id in photoIds.getPhotoIds():
	# 	print id
	print "You have total %s photos" % len(photoIds.getPhotoIds())
else:
	print "API Call Failed"


	

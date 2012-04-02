import vkontakte
vk = vkontakte.API('2877404', '0M0TG9pXnv3ytoMjJHyp')
print vk.getServerTime()

profiles = vk.getProfiles(uids='1,2', fields='education')
pavel = profiles[0]
print pavel['last_name'], pavel['university_name']
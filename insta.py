import instaloader
loader = instaloader.Instaloader()
user = input("Enter your username")

# loader.login("USER", "PASSWORD")   if it's a private account then you have to provide the passowrd
# if i will make it true then only profile pic will downloaded
loader.download_profile(user, profile_pic_only=False)
profile = instaloader.Profile.from_username(loader.context, user)
# print(f"Number of followers: {profile.followers}")   same work as next line


# for finding number of followers
print("Number of followers: {}".format(profile.followers))

media = profile.mediacount
# for finding total number of post
print("Total posts: {}".format(media))


bio = profile.biography
# for printing the bio
print(bio)

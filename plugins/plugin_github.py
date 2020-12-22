import base

print("Processing GitHub...")

header = "# GitHub Start\n"
footer = "# GitHub End\n"

git_ip = base.get_ip("https://github.com.ipaddress.com/")
gist_git_ip = base.get_ip("https://github.com.ipaddress.com/gist.github.com")
asset_cdn_git_ip = base.get_ip("https://github.com.ipaddress.com/assets-cdn.github.com")
asset_git_ip = base.get_ip("https://githubusercontent.com.ipaddress.com/raw.githubusercontent.com")

hosts_append = header + \
    git_ip + "    github.com\n" + \
    gist_git_ip + "    gist.github.com\n" + \
    asset_cdn_git_ip + "    assets-cdn.github.com\n" + \
    asset_git_ip + "    raw.githubusercontent.com\n" + \
    asset_git_ip + "    gist.githubusercontent.com\n" + \
    asset_git_ip + "    cloud.githubusercontent.com\n" + \
    asset_git_ip + "    camo.githubusercontent.com\n" + \
    asset_git_ip + "    avatars0.githubusercontent.com\n" + \
    asset_git_ip + "    avatars1.githubusercontent.com\n" + \
    asset_git_ip + "    avatars2.githubusercontent.com\n" + \
    asset_git_ip + "    avatars3.githubusercontent.com\n" + \
    asset_git_ip + "    avatars4.githubusercontent.com\n" + \
    asset_git_ip + "    avatars5.githubusercontent.com\n" + \
    asset_git_ip + "    avatars6.githubusercontent.com\n" + \
    asset_git_ip + "    avatars7.githubusercontent.com\n" + \
    asset_git_ip + "    avatars8.githubusercontent.com\n" + \
    footer

print(hosts_append)

base.append_hosts(hosts_append)
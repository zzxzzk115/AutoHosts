import base

print("Processing Coursera...")

header = "# Coursera Start\n"
footer = "# Coursera End\n"
hosts_append = header + "52.84.246.90    d3c33hcgiwev3.cloudfront.net\n\
52.84.246.252   d3c33hcgiwev3.cloudfront.net\n\
52.84.246.144   d3c33hcgiwev3.cloudfront.net\n\
52.84.246.72    d3c33hcgiwev3.cloudfront.net\n\
52.84.246.106   d3c33hcgiwev3.cloudfront.net\n\
52.84.246.135   d3c33hcgiwev3.cloudfront.net\n\
52.84.246.114    d3c33hcgiwev3.cloudfront.net\n\
52.84.246.90    d3c33hcgiwev3.cloudfront.net\n\
52.84.246.227    d3c33hcgiwev3.cloudfront.net\n" + footer

print(hosts_append)

base.append_hosts(hosts_append)
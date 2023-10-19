def version_upgrade(curr_version:list):
    added = False
    for i in range(len(curr_version) - 1, -1, -1):
        if curr_version[i] >= 9 and i == len(curr_version) - 1:
            curr_version[i] = 0
            curr_version[i - 1] = curr_version[i - 1] + 1
            added = True
        elif curr_version[i] > 9:
            curr_version[i] = 0
            if i == 0:
                curr_version.insert(0, 1)
                continue
            curr_version[i - 1] = curr_version[i - 1] + 1
        elif not added:
            curr_version[i] = curr_version[i] + 1
            return curr_version
    return curr_version


version_list = input().split(".")
version_list = [int(x) for x in version_list]
print(f".".join(str(x) for x in version_upgrade(version_list)))

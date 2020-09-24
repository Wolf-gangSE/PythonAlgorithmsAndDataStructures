def search(list_, id):
    while True:
        if len(list_) > 1:
            middle = len(list_)//2
            if list_[middle].id == id:
                return list_[middle]
            elif id == 1:
                return list_[0]
            else:
                if list_[middle].id > id:
                    list_ = list_[:middle]
                    continue
                else:
                    list_ = list_[middle:]
                    continue
        else:
            return None
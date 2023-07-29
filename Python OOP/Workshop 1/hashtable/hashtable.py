class HashTable:
    __INITIAL_SIZE = 4

    def __init__(self):
        self.array = [None] * HashTable.__INITIAL_SIZE
        self.keys = [""] * HashTable.__INITIAL_SIZE
        self.total_items = 0

    def _double_arrays_size(self):
        self.array.extend([None] * HashTable.__INITIAL_SIZE)
        self.keys.extend([""] * HashTable.__INITIAL_SIZE)

        HashTable.__INITIAL_SIZE *= 2

    def hash(self, key: str) -> int:
        for index, k in enumerate(self.keys):
            if k == key:
                return index
            elif k == "":
                break

        self.total_items += 1
        return self.total_items - 1

        # self._double_arrays_size()
        # return self.hash(key)

    @staticmethod
    def key_validator(key: str):
        if key.strip() == "":
            raise ValueError(f"Key should be a non empty string")
        return key

    def _check_if_you_need_to_double_array(self):
        return "" not in self.keys

    def add(self, key: str, value):     # Adds a NEW -- Key: Value -- pair
        self.key_validator(key)
        index = self.hash(key)
        self.keys[index] = key
        self.array[index] = value

        if self._check_if_you_need_to_double_array():
            self._double_arrays_size()

    def __find_index_by_key(self, key: str):

        for index, k in enumerate(self.keys):
            if k == key:
                return index

        raise KeyError(f"{key} not in HashTable")

    def remove(self, key: str):
        index = self.__find_index_by_key(key)

        self.keys.pop(index)
        self.keys.append("")

        self.array.pop(index)
        self.array.append(None)

        self.total_items -= 1

    def get(self, key: str):
        return self.array[self.keys.index(key)]

    def __setitem__(self, key: str, value):
        self.add(key, value)

    def __getitem__(self, key: str):
        return self.get(key)

    def __len__(self):
        return self.__INITIAL_SIZE

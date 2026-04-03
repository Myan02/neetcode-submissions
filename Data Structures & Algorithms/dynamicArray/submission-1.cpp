class DynamicArray {
private:
    int* arr;
    int size;
    int capacity;

public:

    // Constructor to initialize array
    DynamicArray(int capacity) : capacity(capacity), size(0) {
        arr = new int[capacity];
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (size == capacity) {
            resize();
        }

        arr[size] = n;
        size++;
    }

    int popback() {
        if (size > 0) {
            size--;
        }

        return arr[size];
    }

    void resize() {
        capacity *= 2;
        int* new_array = new int[capacity];

        for (int i = 0; i < size; i++) {
            new_array[i] = arr[i];
        }

        delete[] arr;
        arr = new_array;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};

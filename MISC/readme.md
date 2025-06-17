# Tài liệu chi tiết về Queue trong C++

## 📋 Mục lục
- [Giới thiệu về Queue](#giới-thiệu-về-queue)
- [Cú pháp khai báo](#cú-pháp-khai-báo)
- [Các phương thức cơ bản](#các-phương-thức-cơ-bản)
- [Ví dụ thực tế](#ví-dụ-thực-tế)
- [Lưu ý quan trọng](#lưu-ý-quan-trọng)
- [Độ phức tạp thời gian](#độ-phức-tạp-thời-gian)
- [Ứng dụng thực tế](#ứng-dụng-thực-tế)
- [So sánh với các cấu trúc khác](#so-sánh-với-các-cấu-trúc-khác)

---

## 🎯 Giới thiệu về Queue

**Queue** (hàng đợi) là một cấu trúc dữ liệu tuyến tính hoạt động theo nguyên tắc **FIFO** (First In, First Out) - phần tử được thêm vào trước sẽ được lấy ra trước.

```
    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
    │  1  │ <- │  2  │ <- │  3  │ <- │  4  │  <- push()
    └─────┘    └─────┘    └─────┘    └─────┘
       ↑                                ↑
    pop()                           back()
   front()
```

### ✨ Đặc điểm chính:
- **FIFO**: Phần tử đầu tiên vào sẽ là phần tử đầu tiên ra
- **Thêm cuối**: Các phần tử mới được thêm vào cuối queue
- **Xóa đầu**: Chỉ có thể xóa phần tử ở đầu queue
- **Truy cập hạn chế**: Chỉ có thể truy cập phần tử đầu và cuối

---

## 🔧 Cú pháp khai báo

### Import thư viện
```cpp
#include <queue>
```

### Khai báo cơ bản
```cpp
std::queue<kiểu_dữ_liệu> tên_queue;
```

### Ví dụ khai báo
```cpp
#include <queue>
#include <string>

std::queue<int> q1;           // Queue chứa số nguyên
std::queue<std::string> q2;   // Queue chứa chuỗi
std::queue<double> q3;        // Queue chứa số thực
std::queue<char> q4;          // Queue chứa ký tự
```

### Khai báo với container tùy chỉnh
```cpp
#include <queue>
#include <list>
#include <deque>

std::queue<int> q1;                         // Mặc định (deque)
std::queue<int, std::list<int>> q2;         // Sử dụng list
std::queue<int, std::deque<int>> q3;        // Sử dụng deque (tường minh)
```

---

## ⚙️ Các phương thức cơ bản

### 1. **push()** - Thêm phần tử
```cpp
queue.push(giá_trị);
```
- **Chức năng**: Thêm phần tử vào cuối queue
- **Tham số**: Giá trị cần thêm
- **Trả về**: void
- **Độ phức tạp**: O(1)

**Ví dụ:**
```cpp
std::queue<int> q;
q.push(10);    // Queue: [10]
q.push(20);    // Queue: [10, 20]
q.push(30);    // Queue: [10, 20, 30]
```

### 2. **pop()** - Xóa phần tử đầu
```cpp
queue.pop();
```
- **Chức năng**: Xóa phần tử ở đầu queue
- **Tham số**: Không có
- **Trả về**: void (không trả về giá trị bị xóa)
- **Độ phức tạp**: O(1)
- **⚠️ Lưu ý**: Không kiểm tra queue rỗng

**Ví dụ:**
```cpp
std::queue<int> q;
q.push(10);    // Queue: [10]
q.push(20);    // Queue: [10, 20]
q.pop();       // Queue: [20] (xóa 10)
```

### 3. **front()** - Truy cập phần tử đầu
```cpp
queue.front();
```
- **Chức năng**: Truy cập phần tử ở đầu queue
- **Tham số**: Không có
- **Trả về**: Tham chiếu đến phần tử đầu
- **Độ phức tạp**: O(1)
- **⚠️ Lưu ý**: Không kiểm tra queue rỗng

**Ví dụ:**
```cpp
std::queue<int> q;
q.push(10);
q.push(20);
std::cout << q.front();  // In ra: 10
q.front() = 100;         // Thay đổi giá trị thành 100
```

### 4. **back()** - Truy cập phần tử cuối
```cpp
queue.back();
```
- **Chức năng**: Truy cập phần tử ở cuối queue
- **Tham số**: Không có
- **Trả về**: Tham chiếu đến phần tử cuối
- **Độ phức tạp**: O(1)

**Ví dụ:**
```cpp
std::queue<int> q;
q.push(10);
q.push(20);
std::cout << q.back();   // In ra: 20
q.back() = 200;          // Thay đổi giá trị thành 200
```

### 5. **empty()** - Kiểm tra rỗng
```cpp
queue.empty();
```
- **Chức năng**: Kiểm tra xem queue có rỗng không
- **Tham số**: Không có
- **Trả về**: bool (true nếu rỗng, false nếu không)
- **Độ phức tạp**: O(1)

**Ví dụ:**
```cpp
std::queue<int> q;
std::cout << q.empty();  // In ra: 1 (true)
q.push(10);
std::cout << q.empty();  // In ra: 0 (false)
```

### 6. **size()** - Lấy kích thước
```cpp
queue.size();
```
- **Chức năng**: Lấy số lượng phần tử trong queue
- **Tham số**: Không có
- **Trả về**: size_t (số lượng phần tử)
- **Độ phức tạp**: O(1)

**Ví dụ:**
```cpp
std::queue<int> q;
std::cout << q.size();   // In ra: 0
q.push(10);
q.push(20);
std::cout << q.size();   // In ra: 2
```

---

## 💡 Ví dụ thực tế

### 1. Queue cơ bản
```cpp
#include <iostream>
#include <queue>

int main() {
    std::queue<int> q;
    
    // Thêm phần tử
    q.push(10);
    q.push(20);
    q.push(30);
    
    std::cout << "Kích thước: " << q.size() << std::endl;
    std::cout << "Phần tử đầu: " << q.front() << std::endl;
    std::cout << "Phần tử cuối: " << q.back() << std::endl;
    
    // Lấy phần tử theo FIFO
    while (!q.empty()) {
        std::cout << q.front() << " ";
        q.pop();
    }
    
    return 0;
}
```

**Output:**
```
Kích thước: 3
Phần tử đầu: 10
Phần tử cuối: 30
10 20 30
```

### 2. Hàng đợi khách hàng
```cpp
#include <iostream>
#include <queue>
#include <string>

int main() {
    std::queue<std::string> customerQueue;
    
    // Khách hàng vào hàng đợi
    customerQueue.push("Nguyễn Văn A");
    customerQueue.push("Trần Thị B");
    customerQueue.push("Lê Văn C");
    
    std::cout << "Số khách hàng đang chờ: " << customerQueue.size() << std::endl;
    
    // Phục vụ khách hàng
    int order = 1;
    while (!customerQueue.empty()) {
        std::cout << order << ". Đang phục vụ: " 
                  << customerQueue.front() << std::endl;
        customerQueue.pop();
        order++;
    }
    
    return 0;
}
```

### 3. Thuật toán BFS (Breadth-First Search)
```cpp
#include <iostream>
#include <queue>
#include <vector>

void bfs(std::vector<std::vector<int>>& graph, int start) {
    std::queue<int> q;
    std::vector<bool> visited(graph.size(), false);
    
    q.push(start);
    visited[start] = true;
    
    std::cout << "BFS từ node " << start << ": ";
    
    while (!q.empty()) {
        int current = q.front();
        q.pop();
        std::cout << current << " ";
        
        // Thêm các node kề chưa thăm
        for (int neighbor : graph[current]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
    std::cout << std::endl;
}

int main() {
    // Đồ thị: 0->[1,2], 1->[3,4], 2->[5]
    std::vector<std::vector<int>> graph = {
        {1, 2},    // Node 0
        {3, 4},    // Node 1
        {5},       // Node 2
        {},        // Node 3
        {},        // Node 4
        {}         // Node 5
    };
    
    bfs(graph, 0);
    return 0;
}
```

### 4. Queue với struct
```cpp
#include <iostream>
#include <queue>
#include <string>

struct Task {
    std::string name;
    int priority;
    
    Task(std::string n, int p) : name(n), priority(p) {}
};

int main() {
    std::queue<Task> taskQueue;
    
    // Thêm task
    taskQueue.push(Task("Backup database", 1));
    taskQueue.push(Task("Send emails", 2));
    taskQueue.push(Task("Generate reports", 3));
    
    // Xử lý task
    while (!taskQueue.empty()) {
        Task current = taskQueue.front();
        std::cout << "Xử lý: " << current.name 
                  << " (Priority: " << current.priority << ")" << std::endl;
        taskQueue.pop();
    }
    
    return 0;
}
```

---

## ⚠️ Lưu ý quan trọng

### 1. Kiểm tra queue rỗng
```cpp
// ✅ AN TOÀN
if (!q.empty()) {
    std::cout << q.front();
    q.pop();
}

// ❌ NGUY HIỂM - Có thể gây lỗi runtime
std::cout << q.front();  // Nếu queue rỗng → undefined behavior
q.pop();                 // Nếu queue rỗng → undefined behavior
```

### 2. pop() không trả về giá trị
```cpp
std::queue<int> q;
q.push(10);

// ❌ SAI - pop() không trả về gì
// int value = q.pop();

// ✅ ĐÚNG - Lấy giá trị trước khi pop
int value = q.front();
q.pop();
```

### 3. Queue không hỗ trợ iterator
```cpp
std::queue<int> q;
// ❌ Không thể làm như này
// for (auto it = q.begin(); it != q.end(); ++it) { ... }

// ✅ Cách duy nhất để duyệt (sẽ xóa các phần tử)
while (!q.empty()) {
    std::cout << q.front() << " ";
    q.pop();
}
```

### 4. Không thể truy cập phần tử ở giữa
```cpp
std::queue<int> q;
q.push(10);
q.push(20);
q.push(30);

// ❌ Không thể làm
// std::cout << q[1];  // Không có operator[]

// ✅ Chỉ có thể truy cập đầu và cuối
std::cout << q.front();  // 10
std::cout << q.back();   // 30
```

---

## ⏱️ Độ phức tạp thời gian

| Phép toán | Độ phức tạp | Ghi chú |
|-----------|-------------|---------|
| `push()` | **O(1)** | Thêm phần tử vào cuối |
| `pop()` | **O(1)** | Xóa phần tử ở đầu |
| `front()` | **O(1)** | Truy cập phần tử đầu |
| `back()` | **O(1)** | Truy cập phần tử cuối |
| `empty()` | **O(1)** | Kiểm tra rỗng |
| `size()` | **O(1)** | Lấy kích thước |

### Không gian bộ nhớ
- **Độ phức tạp không gian**: O(n) với n là số phần tử trong queue

---

## 🚀 Ứng dụng thực tế

### 1. **Thuật toán đồ thị**
- **BFS (Breadth-First Search)**: Duyệt đồ thị theo chiều rộng
- **Tìm đường đi ngắn nhất**: Trong đồ thị không trọng số
- **Level-order traversal**: Duyệt cây theo từng tầng

### 2. **Hệ thống xử lý**
- **Task scheduling**: Lập lịch công việc theo FIFO
- **Print queue**: Hàng đợi in ấn
- **CPU scheduling**: Thuật toán FCFS (First Come First Served)

### 3. **Mô phỏng hệ thống**
- **Queue hệ thống**: Hàng đợi khách hàng, cuộc gọi
- **Buffer**: Đệm dữ liệu trong truyền thông
- **Producer-Consumer**: Mô hình sản xuất-tiêu thụ

### 4. **Game Development**
- **Event queue**: Hàng đợi sự kiện
- **Animation queue**: Hàng đợi hoạt ảnh
- **Message passing**: Truyền tin nhắn giữa các đối tượng

### 5. **Web Development**
- **Request queue**: Hàng đợi yêu cầu HTTP
- **Background jobs**: Công việc chạy nền
- **Cache management**: Quản lý bộ nhớ đệm

---

## 📊 So sánh với các cấu trúc khác

### Queue vs Stack vs Vector

| **Đặc điểm** | **Queue** | **Stack** | **Vector** |
|--------------|-----------|-----------|------------|
| **Nguyên tắc** | FIFO | LIFO | Random Access |
| **Thêm phần tử** | Cuối (push) | Đầu/Cuối (push) | Bất kỳ (insert) |
| **Xóa phần tử** | Đầu (pop) | Đầu/Cuối (pop) | Bất kỳ (erase) |
| **Truy cập** | Đầu + Cuối | Chỉ đầu/cuối | Bất kỳ (index) |
| **Iterator** | ❌ Không | ❌ Không | ✅ Có |
| **Ứng dụng** | BFS, Scheduling | DFS, Undo/Redo | Mảng động |

### Performance Comparison

| **Thao tác** | **Queue** | **Stack** | **Vector** | **List** |
|--------------|-----------|-----------|------------|----------|
| Insert/Push | O(1) | O(1) | O(1) amortized | O(1) |
| Delete/Pop | O(1) | O(1) | O(1) | O(1) |
| Access | O(1) front/back | O(1) top | O(1) random | O(n) |
| Search | O(n) | O(n) | O(n) | O(n) |

---

## 📝 Bài tập thực hành

### Bài 1: Đảo ngược queue
```cpp
// Viết hàm đảo ngược queue sử dụng stack
void reverseQueue(std::queue<int>& q);
```

### Bài 2: Generate binary numbers
```cpp
// Sinh ra n số nhị phân đầu tiên sử dụng queue
void generateBinary(int n);
```

### Bài 3: First non-repeating character
```cpp
// Tìm ký tự đầu tiên không lặp lại trong stream
char firstNonRepeating(std::string stream);
```

---

## 🎯 Tổng kết

Queue là một cấu trúc dữ liệu quan trọng trong C++ với những đặc điểm chính:

### ✅ **Ưu điểm**
- Hiệu quả cho xử lý FIFO
- Các thao tác cơ bản đều O(1)
- Dễ sử dụng và hiểu
- Phù hợp cho nhiều thuật toán

### ❌ **Nhược điểm**
- Không thể truy cập phần tử ở giữa
- Không hỗ trợ iterator
- Không thể duyệt mà không xóa phần tử

### 🎲 **Khi nào sử dụng Queue**
- Cần xử lý dữ liệu theo thứ tự FIFO
- Thuật toán BFS
- Scheduling và task management
- Mô phỏng hàng đợi trong thực tế
- Buffer và caching systems

Queue là công cụ mạnh mẽ và không thể thiếu trong toolkit của mọi lập trình viên C++!
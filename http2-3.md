# <span style="color: #2E8B57">**HTTP/2 vs HTTP/3**</span>

### <div style="text-align: center;">**By Jamie**</div>

---

## <span style="color: #FF6347;">**What is HTTP/3?**</span>

**Hypertext Transfer Protocol (HTTP)** is the fundamental protocol (rules) used for transferring data over the web.
HTTP/3 is the **latest version** of HTTP, designed to address the limitations of **HTTP/2** and enhance web performance.

![alt text](image.png)

### **Key Differences Between HTTP/2 and HTTP/3:**

### <span style="color: #FF4500;">1. **Protocol Used**</span>

- **HTTP/2** uses **TCP** (Transmission Control Protocol) for data transmission.
- **HTTP/3** uses **QUIC** (Quick UDP Internet Connections), which operates over **UDP**.
  This change allows HTTP/3 to overcome some of the limitations of TCP, providing a faster and more efficient connection.

### <span style="color: #FF4500;">2. **Head-of-Line (HOL) Blocking**</span>

- **HTTP/2** suffers from **Head-of-Line (HOL) blocking** issues, where clients must wait for previous requests to finish before sending new ones.
- **HTTP/3** eliminates HOL blocking by allowing **independent streams** within a single connection.

### <span style="color: #FF4500;">3. **Performance Improvements**</span>

- **QUIC** used in HTTP/3 allows for **faster connection establishment** and **better error handling**.
- **HTTP/3** is more resilient to **packet loss** and **network disturbances**, improving overall performance.

### <span style="color: #FF4500;">4. **Connection Migration**</span>

- **HTTP/2** does not support **network migration**. If a connection is lost or interrupted (e.g., switching networks), a new connection must be established.
- **HTTP/3** supports **connection migration**, allowing connections to seamlessly continue, even when the network changes.

### <span style="color: #FF4500;">5. **Congestion Control**</span>

- **HTTP/2** uses TCP-based congestion control mechanisms.
- **HTTP/3** enhances congestion control using QUIC-based protocols, improving overall network management and reducing delays.

### <span style="color: #FF4500;">6. **TLS Encryption**</span>

- **HTTP/2** allows **optional TLS encryption**.
- **HTTP/3** **requires TLS encryption** by default within the **QUIC protocol**, enhancing security.

---

**Conclusion:**
HTTP/3 represents a significant leap forward in web technology, providing **improved speed, security, and resilience** compared to HTTP/2. By addressing key issues like Head-of-Line blocking, connection migration, and congestion control, HTTP/3 aims to create a better browsing experience across the internet.

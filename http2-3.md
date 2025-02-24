# HTTP2 vs HTTP3

## Jamie Isaacs

### What is HTTP3?

Hyper Text Transfer Protocol.
HTTP/3 is the latest version of HTTP, designed to improve upon the limitations of HTTP/2. It aims to enable fast, reliable, and secure web connections across all types of devices.

Key Differences:

1. Protocol Used - HTTP/2 uses TCP (Transmission Control Protocol), while HTTP/3 uses QUIC (Quick UDP Internet Connections), which operates over UDP. This change allows HTTP/3 to overcome some of the limitations of TCP.
2. Head of Line Blocking – HTTP/2 suffers from HOL blocking issues at the transport layer, which refers to the situation in which a browser or client, must wait for previous requests to complete, before sending another. HTTP/3, using QUIC, resolves this by allowing a single connection to have independent streams.
3. Performance – The use of QUIC allows for faster connection establishment and improved error handling, making HTTP/3 more resilient to packet loss and network disturbances.
4. Connection Migration – HTTP/2 does not support network migration, which means that if a connection is interrupted, a new one has to be established. HTTP/3 supports connection migration, allowing connections to seamlessly continue even with network changes.
5. Congestion Control – HTTP/2 relies on TCP-based congestion control mechanisms, while HTTP/3 provides better management of congestion by using QUIC-based congestion control.
6. TLS (Transport Layer Security) Encryption – While TLS encryption is optional in HTTP/2, it is incorporated by default within the QUIC protocol in HTTP/3, enhancing security.

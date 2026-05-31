# qwenpaw-key-decrypt
用于解密qwenpaw被加密后的大模型api-key

## 使用前提
- 需要拥有.master_key密钥文件（一般在/working.secret 文件夹内）
- 需要拥有属于你自己被加密的api-key（正确格式为：ENC:xxxxx）
- 使用前需要安装cryptography库
```pip install
pip install cryptography
```

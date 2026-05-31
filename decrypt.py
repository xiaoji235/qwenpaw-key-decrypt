from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

def derive_key_from_hex(hex_key):
    """从十六进制字符串派生出有效的Fernet密钥"""
    # 将十六进制字符串转换为字节
    key_bytes = bytes.fromhex(hex_key)
    
    # 如果密钥长度不是32字节，则通过哈希处理使其成为32字节
    if len(key_bytes) != 32:
        digest = hashes.Hash(hashes.SHA256())
        digest.update(key_bytes)
        key_bytes = digest.finalize()
    
    # 使用Base64编码使密钥符合Fernet格式
    fernet_key = base64.urlsafe_b64encode(key_bytes)
    return fernet_key

def decrypt_message(master_key_hex, encrypted_message):
    """解密消息"""
    try:
        # 从十六进制密钥派生Fernet密钥
        fernet_key = derive_key_from_hex(master_key_hex)
        
        # 创建Fernet实例
        cipher_suite = Fernet(fernet_key)
        
        # 提取密文（去除"ENC:"前缀）
        if encrypted_message.startswith("ENC:"):
            encrypted_message = encrypted_message[4:]
        
        # 解密消息
        decrypted_message = cipher_suite.decrypt(encrypted_message.encode())
        
        return decrypted_message.decode()
    
    except Exception as e:
        return f"解密失败: {str(e)}"

def main():
    print("Qwenpaw解密工具")
    print("=" * 30)
    
    # 获取用户输入的master_key
    master_key_input = input("请输入.master_key文件中的密钥: ").strip()
    
    # 获取用户输入的密文
    encrypted_input = input("请输入需要解密的内容: ").strip()
    
    # 进行解密
    result = decrypt_message(master_key_input, encrypted_input)
    
    print("\n解密结果:")
    print(result)

if __name__ == "__main__":
    main()

# OpreSiveTEditor

# File Management API with Encryption/Decryption

This project provides a FastAPI-based API for managing files, including functionalities for saving, encrypting, and decrypting file contents using AES encryption.

## Features

- Load file contents and display them in the frontend.
- Save file contents to the specified path, creating the file if it doesn’t exist.
- Encrypt and decrypt file contents using AES encryption.
- Automatic syntax highlighting based on file type.

## Table of Contents

1. [Installation](#installation)
2. [Running the Application](#running-the-application)
3. [API Endpoints](#api-endpoints)
4. [Encryption and Decryption](#encryption-and-decryption)
5. [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jero98772/OpreSiveTEditor
   cd OpreSiveTEditor

   ```

2. **Install required packages**:
   Make sure you have Python 3.7 or higher installed. Create a virtual environment and install the necessary dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install fastapi[all] uvicorn

   ```

## Running the Application

To start the FastAPI application, run the following command in your terminal:

```bash
uvicorn main:app --reload
```

- The application will be available at `http://127.0.0.1:8000`.
- You can access the automatically generated API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Save File

**POST** `/save-file/`

**Request Body**:
```json
{
    "file_path": "path/to/your/file.txt",
    "content": "File content goes here."
}
```

**Response**:
```json
{
    "message": "File saved successfully"
}
```

### Encrypt Content

**POST** `/encrypt/`

**Request Body**:
```json
{
    "key": "your-aes-key",
    "content": "Content to encrypt"
}
```

**Response**:
```json
{
    "encrypted_content": "Encrypted content here"
}
```

### Decrypt Content

**POST** `/decrypt/`

**Request Body**:
```json
{
    "key": "your-aes-key",
    "encrypted_content": "Content to decrypt"
}
```

**Response**:
```json
{
    "decrypted_content": "Decrypted content here"
}
```

## Encryption and Decryption

The application utilizes AES (Advanced Encryption Standard) for encrypting and decrypting file contents. AES is a symmetric encryption algorithm, meaning the same key is used for both encryption and decryption.

### How It Works

1. **Encryption**:
   - The plaintext content is encrypted using the specified AES key, producing ciphertext that can be safely stored or transmitted.

2. **Decryption**:
   - The encrypted content can be decrypted back to its original form using the same AES key.

### Important Note on AES Key
- The AES key must be kept secure. If the key is lost, the encrypted data cannot be recovered.


## Screenshots
![](https://raw.githubusercontent.com/jero98772/OpreSiveTEditor/refs/heads/main/screenshots/1.png)
![](https://raw.githubusercontent.com/jero98772/OpreSiveTEditor/refs/heads/main/screenshots/2.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

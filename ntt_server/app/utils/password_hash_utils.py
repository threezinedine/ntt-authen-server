from pwdlib import PasswordHash


hashUtils = PasswordHash.recommended()


def HashPassword(password: str) -> str:
    return hashUtils.hash(password)


def VerifyPassword(password: str, hashedPassword: str) -> bool:
    return hashUtils.verify(password, hashedPassword)

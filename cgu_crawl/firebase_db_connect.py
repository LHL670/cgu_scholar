import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

service_account={
    "type": "service_account",
    "project_id": "cgusholar",
    "private_key_id": "92aa446e6859f48ae09a1731edfab614fc68c1e0",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDIdbOKyr9Cs6tc\n4VbjGfNp3kWDjfmMQnB9iOWqpxlnlpnwMD1dlZfAeFbSSLyZAIeuyJ9xSBOLOHCN\n1/cRaXIwn98JNI9v7PwKakbWrndQ4NpOS/hcL2zIDWCx2xdlPHBaKTwYBUU9hpiK\nW/DngH6pGM+i1idyL/Tm5+qDHh5wANikatUOGbZ19DOlrBCOGWCMIkpya+XMEl/g\nouUoBh3vgWMs2hpl3K2DqNkipyMCMIKQa0aOAWqJ5u2wDSbQIjh1HYmNRiPy8Lyj\n5aGFXTy2CE2V7B0ypS6+OsIBCONNY/XcJrrZGIT7rqWoaoMRUCJ5kD6FfMZKTDON\n52k2hwjhAgMBAAECggEAFbUP4F+MhD5s4phw7mkbf6M3Ai7IJK+h0H5CvI7uxIBo\nTWcJO3lHtGseSmmKVBkyGDPCdvkX9gitFjcaRUjsDtGTzJfj+89SYGsEyRpIcmTU\nTwvmqk46aJQbnKGTMCkc04Pz7Xf4o60lFz/V3659niBr2lV4HQ3jZnPGZIoeQADY\n5jdPRQfDPs/a6YV9M7+/Lx6m3jashzqB82T2tjz4lJY93hVgZsk+KRTe2eYtNmgl\nnZeyFVE3320Mp+2MuatUp4CBBsKFqdaLt8bPwQO1QqNip5ra3x897lZ0Cd8nXrkY\nhc7IHAubiz4hIWCYDkTo1jGrP2+ATSogYVeMuQPrRwKBgQD1sIBj2Qp9aRCE0sxK\nybOzHm1PdkXvJS3ptey6TqpLYJ/nN7TPJ1cm1tqbEZvM5RIyxMLwsFDNWpdZRML7\noqzvd0g7YoLTuGBZTxxeINQNm6/endzBrX93fAesfmkexvAK8LM6ZCgR7j6Heb6X\nt185N67HLl9D+xRRvzCUA0Of+wKBgQDQ30lu9urjUlArLQRDhOMzLAA9beCLn166\nhxJ1+wsx9KEmkw/chqxanOWGC57SCydE1Tk7ZPTl9Kp5Ks2G4kHUAjjrFzKqbUlM\nnKpapc3l581+96s6MKTBSKqssjPj78wsCLBdbkIN1rKj2TOuKlhBPYJ+3qFhmpOB\nIOVNxR330wKBgFz8pFsl9hZpAVuD/NYBaQXN6kk81lMgmzPtKt+IjmNg+qQkLUaJ\n+S41+x7dlz4BJNYaKj22PZ67PrUGlVVvyEwJtUjki+ddzPmAO5hUjG1qEzIKRVb4\nN1odkznxzg9b89XwK6VZ6uB+byQPK9d4C444SOoR3vR3vsUBu30JjzqpAoGAKet2\nUHfr4l2ly1SIk4h7FM0S60E/HKaKm4L6WIVe1NLU+Onw+ABrXPA6PHHemSc15WGp\nz9rOL8yv3guSHi0Qqx0bEUuhloTCfka/Bdxa+3ZPTtkkG1Sh7EzKPEizk16QKpI/\n2zCCv0ZEqg+wiJblCYrvwsipuO4OBo90lewmvJMCgYBIz2q4UtCNBz573WdtqNHe\n8qNK/rILgKvnchzFi/6mgN3e7tipqmuBgZcsk5AIj469Q4H56z5gYzXhSzlyR6Ul\nrB+1nz5y4qEXIijHwPzYCaXVxCW72geATg+8F43JaaWx+pBJMeya1FBmwyXrj/mf\ncDlbgsQuE6ys4GjXZSJe3w==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-7xdkv@cgusholar.iam.gserviceaccount.com",
    "client_id": "103344934377906835005",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-7xdkv%40cgusholar.iam.gserviceaccount.com"
}
def db():
    if not firebase_admin._apps:
        cred = credentials.Certificate(service_account)
        firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db

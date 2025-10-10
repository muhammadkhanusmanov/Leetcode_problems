from fastapi import FastAPI
import pyodbc
import uuid
import datetime
from pydantic import BaseModel
app = FastAPI()

server = '83.222.6.184'
database = 'demo'
username = 'sa'
password = 'Bt_515822513'
driver = '{FreeTDS}'

@app.get("/")
def home():
    return {"status": "API ishlayapti!"}

@app.get("/medicines/{n}")
def get_medicines(n: int = 10):
    conn_str = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password};TDS_Version=7.4;'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute(f"SELECT TOP {n} _Code, _Description FROM _Reference129;")
    columns = [col[0] for col in cursor.description]
    result = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return result

# to add new item to db
class MedicineCreate(BaseModel):
    code: str
    description: str
    fld130: str
    fld132: str
    fld135: str
    fld136: str
    fld139: str

# 📥 POST — yangi dori qo‘shish
@app.post("/add_dori")
def add_medicine(data: MedicineCreate):
    conn_str = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password};TDS_Version=7.4;'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # 🆔 Unikal ID va version
    _IDRRef = uuid.uuid4().bytes  # unique 16 byte GUID
    _Version = (0).to_bytes(8, 'big')
    _Marked = b'\x00'
    _PredefinedID = b'\x00' * 16
    _Fld133 = b'\x00'
    _Fld140 = datetime.datetime.now()
    _Fld141 = b'\x00'

    insert_query = """
        INSERT INTO _Reference129 
        (_IDRRef, _Version, _Marked, _PredefinedID, _Code, _Description, 
         _Fld130, _Fld131, _Fld132, _Fld133, _Fld134, _Fld135, _Fld136, 
         _Fld137, _Fld138, _Fld139, _Fld140, _Fld141)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    # ⚠️ _Fld131, _Fld134, _Fld137, _Fld138 bo‘sh string bo‘lishi mumkin
    values = (
        _IDRRef,
        _Version,
        _Marked,
        _PredefinedID,
        data.code,
        data.description,
        data.fld130,
        '',
        data.fld132,
        _Fld133,
        '',
        data.fld135,
        data.fld136,
        '',
        '',
        data.fld139,
        _Fld140,
        _Fld141
    )

    cursor.execute(insert_query, values)
    conn.commit()
    conn.close()

    return {"message": "✅ Yangi dori qo'shildi", "code": data.code, "description": data.description}

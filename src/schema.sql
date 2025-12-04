CREATE TABLE customers(
    id_cliente INT PRIMARY KEY,
    nome_completo VARCHAR(50),
    email VARCHAR (50),
    data_cadastro DATE
);


CREATE TABLE sales(
    Invoice VARCHAR,
    StockCode VARCHAR,
    Sales_Description  TEXT,
    Quantity INTEGER,
    InvoiceDate DATE,
    Price REAL,
    Customer_ID INTEGER,
    Country VARCHAR
);

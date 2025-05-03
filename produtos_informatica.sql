CREATE DATABASE IF NOT EXISTS loja_tecnologia;
USE loja_tecnologia;

DROP TABLE IF EXISTS produtos;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    preco DECIMAL(10,2),
    descricao TEXT
);

INSERT INTO produtos (nome, categoria, preco, descricao) VALUES
('Notebook Dell Inspiron 15', 'Notebook', 3999.90, 'Notebook com Intel Core i5, 8GB RAM, 256GB SSD'),
('Mouse Logitech M170', 'Mouse', 79.90, 'Mouse sem fio com conexão USB e tecnologia óptica'),
('Teclado Mecânico Redragon Kumara', 'Teclado', 199.90, 'Teclado mecânico com switches Outemu Blue'),
('Fone JBL Tune 510BT', 'Fone de Ouvido', 249.99, 'Fone bluetooth com bateria de até 40h'),
('Monitor LG 24MK430H', 'Monitor', 849.00, 'Monitor Full HD 24" com HDMI e VGA'),
('Notebook Acer Aspire 5', 'Notebook', 3299.00, 'Notebook com Ryzen 5, 8GB RAM, 512GB SSD'),
('Mouse Gamer Razer DeathAdder', 'Mouse', 299.90, 'Mouse gamer com 6400 DPI e design ergonômico'),
('Teclado Sem Fio Logitech K270', 'Teclado', 129.00, 'Teclado sem fio com receptor USB nano'),
('Headset Gamer HyperX Cloud Stinger', 'Fone de Ouvido', 299.90, 'Headset com microfone giratório e som estéreo'),
('Monitor Samsung 27" Curvo', 'Monitor', 1349.00, 'Monitor curvo com taxa de atualização de 75Hz');

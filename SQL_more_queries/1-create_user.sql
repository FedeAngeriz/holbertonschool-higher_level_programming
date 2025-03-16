-- Creacion de Usuario en Servidor
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_password';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
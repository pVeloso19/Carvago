-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema carvago
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema carvago
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `carvago` DEFAULT CHARACTER SET utf8 ;
USE `carvago` ;

-- -----------------------------------------------------
-- Table `carvago`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `carvago`.`User` (
  `idUser` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NULL,
  `Email` VARCHAR(255) NOT NULL,
  `Password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUser`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `carvago`.`Filtros_Notificacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `carvago`.`Filtros_Notificacao` (
  `idFiltros` INT NOT NULL AUTO_INCREMENT,
  `AnoMinimo` INT NULL,
  `AnoMaximo` INT NULL,
  `PrecoMinimo` FLOAT NULL,
  `PrecoMaximo` FLOAT NULL,
  `Combustivel` VARCHAR(45) NULL,
  `KM_Minimo` INT NULL,
  `KM_Maximo` INT NULL,
  PRIMARY KEY (`idFiltros`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `carvago`.`Carros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `carvago`.`Carros` (
  `idCarros` INT NOT NULL AUTO_INCREMENT,
  `Anunciante` VARCHAR(45) NULL,
  `Marca` VARCHAR(45) NOT NULL,
  `Modelo` VARCHAR(45) NOT NULL,
  `Versao` VARCHAR(45) NULL,
  `Combustivel` VARCHAR(45) NULL,
  `Mes_Registo` VARCHAR(45) NULL,
  `Ano` INT NULL,
  `Quilometros` INT NULL,
  `Cilindrada` INT NULL,
  `Potencia` INT NULL,
  `Cor` VARCHAR(45) NULL,
  `Tipo_Cor` VARCHAR(45) NULL,
  `Tipo_Caixa` VARCHAR(45) NULL,
  `Num_Portas` INT NULL,
  `Origem` VARCHAR(45) NULL,
  `Condicao` VARCHAR(45) NULL,
  `Preco` FLOAT NOT NULL,
  `Link_foto` MEDIUMTEXT NULL,
  `Titulo` VARCHAR(300) NULL,
  `Link_anuncio` VARCHAR(255) NOT NULL,
  `ID_Anuncio` BIGINT(15) NOT NULL,
  `Fonte` VARCHAR(45) NOT NULL,
  `Data` DATETIME(6) NOT NULL,
  PRIMARY KEY (`idCarros`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `carvago`.`Carros_Nao_Vistos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `carvago`.`Carros_Nao_Vistos` (
  `User_idUser` INT NOT NULL,
  `Carros_idCarros` INT NOT NULL,
  PRIMARY KEY (`User_idUser`, `Carros_idCarros`),
  INDEX `fk_Carros_Nao_Vistos_Carros1_idx` (`Carros_idCarros` ASC) VISIBLE,
  CONSTRAINT `fk_Carros_Nao_Vistos_User1`
    FOREIGN KEY (`User_idUser`)
    REFERENCES `carvago`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Carros_Nao_Vistos_Carros1`
    FOREIGN KEY (`Carros_idCarros`)
    REFERENCES `carvago`.`Carros` (`idCarros`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `carvago`.`Interesse`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `carvago`.`Interesse` (
  `User_idUser` INT NOT NULL,
  `Marca` VARCHAR(45) NOT NULL,
  `Modelo` VARCHAR(45) NOT NULL,
  `Fonte` VARCHAR(45) NOT NULL,
  `Filtros_Notificacao_idFiltros` INT NULL,
  PRIMARY KEY (`User_idUser`, `Marca`, `Modelo`, `Fonte`),
  INDEX `fk_Interesses_User1_idx` (`User_idUser` ASC) VISIBLE,
  INDEX `fk_Interesse_Filtros_Notificacao1_idx` (`Filtros_Notificacao_idFiltros` ASC) VISIBLE,
  CONSTRAINT `fk_Interesses_User1`
    FOREIGN KEY (`User_idUser`)
    REFERENCES `carvago`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Interesse_Filtros_Notificacao1`
    FOREIGN KEY (`Filtros_Notificacao_idFiltros`)
    REFERENCES `carvago`.`Filtros_Notificacao` (`idFiltros`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `carvago`.`Favorito`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `carvago`.`Favorito` (
  `User_idUser` INT NOT NULL,
  `Carros_idCarros` INT NOT NULL,
  PRIMARY KEY (`User_idUser`, `Carros_idCarros`),
  INDEX `fk_Favorito_Carros1_idx` (`Carros_idCarros` ASC) VISIBLE,
  CONSTRAINT `fk_Favorito_User1`
    FOREIGN KEY (`User_idUser`)
    REFERENCES `carvago`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Favorito_Carros1`
    FOREIGN KEY (`Carros_idCarros`)
    REFERENCES `carvago`.`Carros` (`idCarros`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


-- -----------------------------------------------------
-- INSERT DADOS INICIAIS
-- -----------------------------------------------------

INSERT INTO carvago.User
	VALUES
    (default, 'Miguel Veloso', 'miguelveloso@mail.pt', 'Pedro1234');

INSERT INTO carvago.Filtros_Notificacao
	VALUES
    (default, 2019,NULL,NULL,NULL,'Gasolina',NULL,NULL);

INSERT INTO carvago.Interesse
	VALUES
    (1, 'ford', 'focus', 'stand-virtual', 1)
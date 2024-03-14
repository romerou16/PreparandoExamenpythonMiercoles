create database Universidad
use Universidad
create table Materias(
cod_asignatura int primary key,
asignaturas varchar(20))

create table Docentes(
ID_profesor bigint primary key,
profesor varchar(80))

create table Departamentos(
ID_departamento int primary key,
departamento varchar(15),
ID_profesor bigint
constraint apodo foreign key(ID_profesor)
references Docentes(ID_profesor))

create table Carreras(
ID_carrera int primary key,
titulacion varchar(20))

create table MateriasCarrera(
cod_asignatura int,
ID_carrera int,
constraint apodo1 foreign key(cod_asignatura) references Materias(cod_asignatura),
constraint apodo4 foreign key(ID_carrera) references Carreras (ID_carrera))

create table MateriasDocente(
cod_asignatura int,
ID_profesor bigint,
constraint apodo2 foreign key(cod_asignatura) references Materias(cod_asignatura),
constraint apodo3 foreign key(ID_profesor) references Docentes(ID_profesor))
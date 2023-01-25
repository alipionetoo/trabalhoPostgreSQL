CREATE TABLE funcionario (
    cpf varchar(11) UNIQUE PRIMARY KEY,
    dnr INTEGER,
    salario float);

CREATE TABLE departamento (
    dnumero INTEGER PRIMARY KEY,
    cpf_ger varchar(11));

CREATE TABLE projeto (
    projenumero INTEGER PRIMARY KEY,
    projlocal varchar(100),
    dnum INTEGER);

CREATE INDEX IF NOT EXISTS "SAL_FUNC"
    ON public. funcionario USING btree
    (salario ASC NULLS LAST) 
    TABLESPACE pg_default;

CREATE INDEX IF NOT EXISTS "CPF_FUNC"
    ON public. funcionario USING btree 
    (cpf COLLATE pg_catalog."default" ASC NULLS LAST) 
    TABLESPACE pg_default;

CREATE INDEX IF NOT EXISTS "PROJE_PLOC" 
    ON public.projeto USING btree
    (projlocal COLLATE pg_catalog. "default" ASC NULLS LAST)
    TABLESPACE pg_default;
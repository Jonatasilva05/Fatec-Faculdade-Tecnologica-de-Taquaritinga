CREATE OR REPLACE PROCEDURE calcular_bono(p_id_funcionario NUMBER) IS
    v_desempenho NUMBER;
    v_salario    NUMBER;
    v_bonus      NUMBER;
BEGIN
    -- Verificar o desempenho do funcionário
    SELECT desempenho, salario INTO v_desempenho, v_salario
    FROM funcionarios
    WHERE id = p_id_funcionario;

    -- Calcular o bônus com base nas regras de desempenho
    IF v_desempenho > 8 THEN
        v_bonus := v_salario * 0.20;
    ELSIF v_desempenho BETWEEN 5 AND 8 THEN
        v_bonus := v_salario * 0.10;
    ELSE
        v_bonus := 0;
    END IF;

    -- Atualizar o salário com o bônus calculado
    UPDATE funcionarios
    SET salario = salario + v_bonus
    WHERE id = p_id_funcionario;

    COMMIT;
END;

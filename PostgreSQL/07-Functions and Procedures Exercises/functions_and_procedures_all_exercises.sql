-- 01. User-defined Function Full Name

CREATE FUNCTION fn_full_name(first_name VARCHAR, last_name VARCHAR)
RETURNS VARCHAR
AS
$$
    DECLARE result VARCHAR;
    BEGIN
        result := CONCAT(INITCAP(first_name), ' ', INITCAP(last_name));
        RETURN result;
    END;
$$
LANGUAGE plpgsql;



-- 02. User-defined Function Future Value

CREATE OR REPLACE FUNCTION fn_calculate_future_value(initial_sum FLOAT, yearly_interest_rate FLOAT, number_of_years INT)
RETURNS NUMERIC
AS
$$
    DECLARE result NUMERIC;
    BEGIN
        result := initial_sum * (POWER(1 + yearly_interest_rate, number_of_years));
        result := TRUNC(result, 4);
        RETURN result;
    END;
$$
LANGUAGE plpgsql;

-- 03. User-defined Function Is Word Comprised




-- 04. Game Over


CREATE OR REPLACE FUNCTION fn_is_game_over(
    is_game_over BOOLEAN
)
RETURNS TABLE (
    name VARCHAR(50),
    game_type_id INT,
    is_finished BOOLEAN
) AS
$$
BEGIN
    RETURN QUERY
    SELECT g.name, g.game_type_id, g.is_finished
    FROM public.games AS g
    WHERE g.is_finished = is_game_over;
END;
$$ LANGUAGE plpgsql;

-- 05. Difficulty Level



-- 06. Cash in User Games Odd Rows✶



-- 08. Deposit Money


CREATE OR REPLACE PROCEDURE sp_deposit_money(account_id INT, money_amount NUMERIC(10, 4))
AS
$$
    DECLARE compare_balance NUMERIC;

    BEGIN
        compare_balance := (SELECT balance FROM accounts WHERE id = account_id) + money_amount;
        UPDATE accounts
        SET balance = balance + money_amount
        WHERE id = account_id;
        IF (SELECT balance FROM accounts WHERE id = account_id) != compare_balance THEN ROLLBACK;
        ELSE COMMIT;
        RETURN ;
        END IF;
    END;
$$
LANGUAGE PLPGSQL;

-- 09. Withdraw Money



-- 10. Money Transfer



-- 11. Delete Procedure



-- 12. Log Accounts Trigger



-- 13. Notification Email on Balance Change
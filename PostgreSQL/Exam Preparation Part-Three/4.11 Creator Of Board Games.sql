CREATE OR REPLACE FUNCTION fn_creator_with_board_games(name VARCHAR(30))
RETURNS INT
AS
$$
    DECLARE total_games INT;
    BEGIN
        SELECT
            COUNT(cbg.board_game_id) AS total
        FROM
            creators AS c
        JOIN
            creators_board_games AS cbg ON cbg.creator_id = c.id
        WHERE
            c.first_name = name
        INTO total_games;
    RETURN total_games;
    END;
$$
LANGUAGE plpgsql;
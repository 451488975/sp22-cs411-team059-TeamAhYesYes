DELIMITER //
CREATE TRIGGER `DISCOUNTING` BEFORE INSERT ON `customer` FOR EACH ROW
    BEGIN
    SET @recommender_count = (
        SELECT COUNT(username)
        FROM `customer`
        GROUP BY `username`
        HAVING `username` = NEW.recommender_name
    );
    IF (@recommender_count > 0) THEN
        SET NEW.discount = 0.9;
    END IF;
END;//
DELIMITER ;

DELIMITER &&
CREATE PROCEDURE update_discount()
BEGIN
	DECLARE varCustomerId INT;
	DECLARE varTotalPurchaseValue DOUBLE;
    DECLARE varRecommendedUserCount INT;
    DECLARE varNewDiscount REAL;
	DECLARE loop_exit BOOLEAN DEFAULT FALSE;
    DECLARE cur CURSOR FOR (
        SELECT customer_id, SUM(total_price) as TotalPurchaseValue
        FROM customer NATURAL JOIN p_order
        GROUP BY customer_id
    );
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET loop_exit = TRUE;

    OPEN cur;
    cloop: LOOP
		FETCH cur INTO varCustomerId, varTotalPurchaseValue;
        SET varRecommendedUserCount =(
            SELECT count(*)
            FROM customer c1, customer c2
            WHERE c1.username = c2.recommender_name AND c1.customer_id = varCustomerId
            GROUP BY c1.username
        );
        IF loop_exit THEN
			LEAVE cloop;
		END IF;

        IF (varTotalPurchaseValue >= 500) OR (varRecommendedUserCount >= 3) THEN
			SET varNewDiscount = 0.7;
		ELSEIF (varTotalPurchaseValue >= 400) OR (varRecommendedUserCount >= 2) THEN
			SET varNewDiscount = 0.8;
        ELSEIF (varTotalPurchaseValue >= 300) OR (varRecommendedUserCount >= 1) THEN
			SET varNewDiscount = 0.9;
        ELSE
			SET varNewDiscount = 1;
        END IF;

        UPDATE customer
		SET discount = varNewDiscount
        WHERE customer_id = varCustomerId;

	END LOOP cloop;
    CLOSE cur;
END&&
DELIMITER ;

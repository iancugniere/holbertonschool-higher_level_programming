-- Lists all the cities of California in hbtn_0d_usa
SELECT id, name FROM cities
		WHERE state_id IN (
			SELECT states.id
			FROM states
			WHERE name = 'California'
		)
		ORDER BY id ASC;

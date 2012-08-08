<?php

/**
 * SERVERNAME	localhost
 * USERNAME		pybros
 * PASSWORD		getIn2it
 * DATABASE		pybros
 */

/**
 * Returns a mysql connection or dies if error occurs
 */
function connect() {
	$con = mysql_connect('localhost', 'pybros', 'getIn2it');

	if (!$con) {
		die('Could not connect to database: ' . mysql_error());
	}

	mysql_select_db('rev4', $con);

	return $con;
}

/**
 * Closes a mysql connection
 */
function disconnect($connection) {
	mysql_close($connection);
}

?>

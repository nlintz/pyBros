<?
// clean.php

/**
 * Returns an escaped character sequence for sql queries
 */
function clean($query) {
	return mysql_real_escape_string($query);
}

?>

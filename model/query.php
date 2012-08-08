<?php
// query.php

/**
 * Notes: No need to specify connection in the query
 */

require_once 'clean.php';

/**
 * Returns a single node by its nid
 */
function get_node_by_id($node_id) {
	$nid = clean($node_id);
	$q = "SELECT *
		FROM nodes
		WHERE nid='$nid'";
	$r = mysql_query($q);
	// TODO error checking
	return mysql_fetch_assoc($r);
}

/**
 * Returns a single node by its jitid
 */
function get_node_by_jitid($jitId) {
	$jitid = clean($jitId);
	$q = "SELECT * 
		FROM nodes
		WHERE jitid='$jitid'";
	$r = mysql_query($q);
	return mysql_fetch_assoc($r);
}

/**
 * Returns a table that represents all the children of $parent_id
 */
function get_childs_by_pid($parent_id) {
	$pid = clean($parent_id);
	$q = "SELECT *
		FROM relations
		WHERE pid='$pid'";
	$r = mysql_query($q);
	$tbl = array();
	$i = 0;
	while ($row = mysql_fetch_assoc($r)) {
		$tbl[$i++] = $row;
	}
	return $tbl;
}

/**
 * Returns a single node, that is the parent of $child_id
 */
function get_parent_by_chid($child_id) {
	$chid = clean($child_id);
	$q = "SELECT nodes.*
		FROM nodes
		INNER JOIN childs
		ON nodes.nid=relations.pid
		WHERE relations.chid='$chid'";
	$r = mysql_query($q);
	return mysql_fetch_assoc($r);
}

?>

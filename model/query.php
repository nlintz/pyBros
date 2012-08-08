<?php
// query.php

/**
 * Notes: No need to specify connection in the query
 */

require_once 'clean.php';

/**
 * Returns a single node by its nid
 */
function select_node_by_id($node_id) {
	$nid = clean($node_id);

	$q = "SELECT name, value
		FROM node_attrs
		WHERE node_id='$nid'";
	$r = mysql_query($q);

	$node = array();

	// TODO error checking
	while ($row = mysql_fetch_assoc($r)) {
		$node[$row['name']] = $row['value'];
	}

	return $node;
}

/**
 * Returns a table that represents all the children of $parent_id
 */
function select_children_by_pid($parent_id) {
	$pid = clean($parent_id);

	$q = "SELECT node_attrs.node_id, node_attrs.name, node_attrs.value
		FROM node_attrs
		INNER JOIN edges
		ON node_attrs.node_id=edges.child_id
		WHERE edges.parent_id='$pid'";
	$r = mysql_query($q);

	// tbl keys are the node_ids, values are assoc arrays 
	$tbl = array();
	while ($row = mysql_fetch_assoc($r)) {
		$id = $row['node_id'];
		if (array_key_exists($id, $tbl)) {
			$tbl[$id][ $row['name'] ] = $row['value'];
		}
		else {
			$tbl[$id] = array( $row['name'] => $row['value'] );
		}
	}

	return $tbl;
}

/**
 * Returns a single node, that is the parent of $child_id
 */
function select_parent_by_chid($child_id) {
	$chid = clean($child_id);

	$q = "SELECT node_attrs.name, node_attrs.value
		FROM node_attrs
		INNER JOIN edges
		ON node_attrs.node_id=edges.parent_id
		WHERE edges.child_id='$chid'";
	$r = mysql_query($q);

	$node = array();

	while ($row = mysql_fetch_assoc($r)) {
		$node[$row['name']] = $row['value'];
	}

	return $node;
}

?>

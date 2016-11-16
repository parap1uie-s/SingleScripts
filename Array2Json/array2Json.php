<?php 
	$data = array('name'=>'aaa','age'=>'23');
	$position = array('name'=>'/user/','age'=>'/user/detail/');

	//Format the logic tree
	$jsonTree = array('name'=>'','age'=>'');
	foreach ($position as $k1 => $v1) {
		$tempTree = explode('/', $v1);
		foreach ($tempTree as $k2 => $v2){
			if($k2 == 0 && strlen($v2) !== 0)
				die('syntax error'.PHP_EOL);
			if(strlen($v2) !==0)
				$jsonTree[$k1][] = $v2;
		}
	}	
	
	// make the json str
	$result = array();
	foreach ($jsonTree as $k1 => $v1) {
		$temp = createChild($jsonTree[$k1],0,$k1,$data[$k1]);
		$result = mergeChild($result,$temp);
	}
	echo json_encode($result).PHP_EOL;

	function createChild($arr,$i,$key,$value){
		if(isset($arr[$i+1]))
			return array($arr[$i]=>createChild($arr,$i+1,$key,$value));
		else
			return array($arr[$i]=>array($key=>$value));
	}

	function mergeChild($arr,$temp){
		foreach ($temp as $key => $value) {
			if(isset($arr[$key]))
				$arr[$key]=mergeChild($arr[$key],$value);
			else
				$arr[$key]=$value;
		}
		return $arr;
	}
 ?>

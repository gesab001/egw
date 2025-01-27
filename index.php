<?php




$topic_param = $_GET['topic'];



function getTotalParagraphs($topic){
	$booklist_url = "https://gesab001.github.io/assets/egw/booklist.json"; 
    $json = file_get_contents($booklist_url);
    $booklist_obj = json_decode( $json, true );
	$total = 0;
    foreach ($booklist_obj["items"] as $x) {
		$bookcode = strtolower($x["bookcode"]);

		if ($topic==$bookcode){
		  $total = $x["total"];
		}
	}
	return $total;
}
function getBookcode($topic){
	$booklist_url = "https://gesab001.github.io/assets/egw/booklist.json"; 
    $json = file_get_contents($booklist_url);
    $booklist_obj = json_decode( $json, true );
	$bookcode = "";
    foreach ($booklist_obj["items"] as $x) {
		$bookcode_string = strtolower($x["bookcode"]);

		if ($topic==$bookcode_string){
		  $bookcode = $x["bookcode"];

		}
	}
	return $bookcode;
}

function getCurrentEgwId($total){
	$now = time(); // or your date as well
	//echo  date('m/d/Y', $now);
	echo $now;
	$your_date = strtotime("2018-05-22");
	$datediff = $now - $your_date;
	echo "$datediff " . $datediff;

	$daysdiff = round($datediff /60/60/24);
	echo "$daysdiff " . $daysdiff;

	$currentID = $daysdiff % $total;
	return $currentID;
}

function getParagraphString($url){
   $json_obj = file_get_contents($url);
   $paragraph_obj = json_decode( $json_obj);
   return $paragraph_obj;   
}

$topic = strtolower($topic_param);
$total = getTotalParagraphs($topic);

$currentID = getCurrentEgwId($total);
$bookcode = getBookcode($topic);
$paragraph_url = "https://gesab001.github.io/assets/egw/" . $bookcode ."/" ."book_".$bookcode."_id_".$currentID.".json";
$paragraph_obj = getParagraphString($paragraph_url);
$word = $paragraph_obj->{'word'};
$paragraph_no = $paragraph_obj->{'paragraph'};
$bookcode_original = $paragraph_obj->{'bookcode'};
$page = $paragraph_obj->{'page'};

echo $word . " (" . $bookcode_original . ", " . $page . ", " . $paragraph_no . ")" ;


?>
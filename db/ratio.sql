SELECT   file_name, 
         bitrate_Mbps, 
		 film_length_m, 
		 film_type,
         (bitrate_Mbps / film_length_m) AS ratio
FROM     file_list
ORDER BY ratio DESC
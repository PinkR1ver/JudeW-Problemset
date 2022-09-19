package HashmapSolution;

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;

public class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        HashMap<String, List<String>> map = new HashMap<>();
        for (String path : paths) {
            String[] file = path.split(" ");
            String root = file[0] + '/';
            for (int i = 1; i < file.length; i++) {
                String[] fileNameAndContent = file[i].split("\\(");
                String fileName = root + fileNameAndContent[0];
                String fileContent = fileNameAndContent[1];
                if (map.containsKey(fileContent)) {
                    map.get(fileContent).add(fileName);
                }
                else {
                    List<String> fileNameList = new ArrayList<>();
                    fileNameList.add(fileName);
                    map.put(fileContent, fileNameList);
                }
            }
        }
        
        List<List<String>> res = new ArrayList<List<String>>();

        for (List<String> value : map.values()) {
            if(value.size() > 1){
                res.add(value);
            }
        }

        return res;

    }
}
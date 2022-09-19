package solutionPackage;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        List<List<String>> res = new ArrayList<List<String>>();
        List<String[]> fileList = new ArrayList<String[]>();
        for (String path : paths) {
            String[] file = path.split(" ");
            String root = file[0] + '/';
            for (int i = 1; i < file.length; i++) {
                String[] fileNameAndContent = file[i].split("\\(");
                String fileName = fileNameAndContent[0];
                String fileContent = fileNameAndContent[1];
                String[] fileset = new String[] {root + fileName, fileContent, "0"};
                fileList.add(fileset);
            }
        }


        for (int i = 0; i < fileList.size() - 1; i++) {
            List<String> tmp = new ArrayList<String>();
            for (int j = i + 1; j < fileList.size(); j++) {
                if(fileList.get(i)[1].equals(fileList.get(j)[1])) {
                    if(fileList.get(i)[2].equals("0")) {
                        tmp.add(fileList.get(i)[0]);
                        fileList.get(i)[2] = "1";
                    }

                    if(fileList.get(j)[2].equals("0")) {
                        tmp.add(fileList.get(j)[0]);
                        fileList.get(j)[2] = "1";
                    }
                }
            }
            boolean ans = tmp.isEmpty();
            if(ans == false){
                res.add(tmp);
            }
        }

        return res;

    }
}
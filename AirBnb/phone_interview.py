'''
Question:
given an array of house listing ordered by listing_id, now we want to print only
12 per webpage. However, we don't want to show the houses with same host_id in
the same page. For example, listing_id 28 and 16 should not be in the same page.
So we move 16 to next page.

Print the listing in each page, seperated by an empty line.
'''

input_csv_array = [
  "host_id,listing_id,score,city",
  "1,28,300.1,San Francisco",
  "4,5,209.1,San Francisco",
  "20,7,208.1,San Francisco",
  "23,8,207.1,San Francisco",
  "16,10,206.1,Oakland",
  "1,16,205.1,San Francisco",
  "6,29,204.1,San Francisco",
  "7,20,203.1,San Francisco",
  "8,21,202.1,San Francisco",
  "2,18,201.1,San Francisco",
  "2,30,200.1,San Francisco",  
  "15,27,109.1,Oakland",
  "10,13,108.1,Oakland",
  "11,26,107.1,Oakland",
  "12,9,106.1,Oakland",
  "13,1,105.1,Oakland",
  "22,17,104.1,Oakland",
  "1,2,103.1,Oakland",
  "28,24,102.1,Oakland",
  "18,14,11.1,San Jose",
  "6,25,10.1,Oakland",
  "19,15,9.1,San Jose",
  "3,19,8.1,San Jose",
  "3,11,7.1,Oakland",
  "27,12,6.1,Oakland",
  "1,3,5.1,Oakland",
  "25,4,4.1,San Jose",
  "5,6,3.1,San Jose",
  "29,22,2.1,San Jose",
  "30,23,1.1,San Jose"
]


MAX_PER_PAGE = 12

def pageProcessor(input):
    hash_table = []
    candidates = []

    result = []
    for i in xrange(0,len(input)):
        str = input[i]
        row = str.split(',')
        host_id = row[0]
        
        if len(result) == MAX_PER_PAGE:
            rest = candidates + input[i:]
            return result + [''] +pageProcessor(rest)
        if host_id in hash_table:
            candidates.append(str)
        else:
            hash_table.append(host_id)
            result.append(str)
            
    result += candidates
    if len(result) < MAX_PER_PAGE:
        return result
    else:
        return result[:MAX_PER_PAGE] + [''] + result[MAX_PER_PAGE:]
  
results = pageProcessor(input_csv_array[1:])
for row in results:
    print row

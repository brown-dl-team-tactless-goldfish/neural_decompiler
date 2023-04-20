public class Solution {
    public string ValidIPAddress(string IP) {
        string IPV4 = "IPv4",
               IPV6 = "IPv6",
               INVALID = "Neither";
        
        if (IP == null || IP == string.Empty)
            return INVALID;
        
        string[] ranges = IP.IndexOf('.') != -1 ? IP.Split('.') : IP.IndexOf(':') != -1 ? IP.Split(':') : null;
        
        if (ranges != null)
            if (IP.IndexOf('.') != -1)
            {
                if (ranges.Length != 4)
                    return INVALID;
                
                foreach (var item in ranges)
                {
                    if (item.Length == 0 || item.Length > 3)
                        return INVALID;
                    
                    foreach (var c in item)
                        if (c < '0' || c > '9')
                            return INVALID;
                    
                    if (Convert.ToInt32(item) > 255 || item.Length > 1 && item[0] == '0')
                        return INVALID;
                }
                        
                return IPV4;
            }
            else
            {
                if (ranges.Length != 8)
                    return INVALID;
                
                foreach (var item in ranges)
                {
                    if (item.Length == 0 || item.Length > 4)
                        return INVALID;
                    
                    foreach (var c in item)
                        if ((c < '0' || c > '9') && (c < 'a' || c > 'f') && (c < 'A' || c > 'F'))
                            return INVALID;
                }
                
                return IPV6;
            }
        
        return INVALID;
    }
}
from reading_files.read_std import read_std
from reduce_functions.sent_data import getSentGb
from reduce_functions.amount_of_requests import getAmountOfRequests200, getAmountOfRequests302, getAmountOfRequests404
from reduce_functions.max_resource import get_max_resource_and_path
from reduce_functions.graphic_downloads import get_ratio_of_graphic_downloads
from present_data import print_output

if __name__ == '__main__':
    read_std()
    print_output(SENT_GB=getSentGb(), AMOUNT_OF_REQUESTS_OF_200=getAmountOfRequests200(),
                 AMOUNT_OF_REQUESTS_OF_404=getAmountOfRequests404(), AMOUNT_OF_REQUESTS_OF_302=getAmountOfRequests302(),
                 MAX_RESOURCE_AND_PATH=get_max_resource_and_path(), RATIO_GRAPHIC=get_ratio_of_graphic_downloads())

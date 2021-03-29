import time

import pytest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from TestData.LoginData import LoginData
from pageObjects.AddMultipleProductToList import AddMultipleProductToList
from pageObjects.AddProductList import AddProductList
from pageObjects.AutoListPlaceOrder import AutoListPlaceOrder
from pageObjects.AutomaticListPage import AutomaticListPage
from pageObjects.CancelOrder import CancelOrder
from pageObjects.CartPage import CartPage
from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.DeleteAutoList import DeleteAutoList
from pageObjects.DeleteManualList import DeleteManualList
from pageObjects.DeteleAutoListWithProduct import DeteleAutoListWithProduct
from pageObjects.HomePage import HomePage
from pageObjects.IllustrationPage import IllustrationPage
from pageObjects.LoginPage import LoginPage
from pageObjects.ManualListPlaceOrder import ManualListPlaceOrder
from pageObjects.MoveProductsToList import MoveProductsToList
from pageObjects.MyAccountPage import MyAccountPage
from pageObjects.MyAddressPage import MyAddressPage
from pageObjects.MyOrdersPage import MyOrdersPage
from pageObjects.MyWishListPage import MyWishListPage
from pageObjects.OrdersPage import OrdersPage
from pageObjects.PlaceOrderPage import PlaceOrderPage
from pageObjects.PopupMessages import PopupMessages
from pageObjects.SearchPage import SearchPage
from pageObjects.StoreSelectionPage import StoreSelectionPage
from pageObjects.ViewManualListProduct import ViewManualListProduct
from pageObjects.WalletPage import WalletPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        illustration = IllustrationPage(self.driver)
        illustration.skip().click()
        action = ActionChains(self.driver)
        storeselection = StoreSelectionPage(self.driver)
        stores = storeselection.activeStores()
        for store in stores:
            action.move_to_element(store).perform()
            time.sleep(3)
            storeselection.storeShopNow().click()
            log.info("In Home Screen")
            break

    def test_login(self, getData):
        loginObj = LoginPage(self.driver)
        log = self.getLogger()
        loginObj.loginIcon().click()
        loginObj.enterUsername().send_keys(getData["username"])
        loginObj.enterPassword().send_keys(getData["password"])
        log.info("Username : " + getData["username"])
        log.info("Username : " + getData["password"])
        loginObj.lButton().click()
        time.sleep(2)

    def test_popupmsg(self):
        log = self.getLogger()
        popMsg = PopupMessages(self.driver)
        msg = popMsg.getMsg().text
        log.info(msg)
        assert "uccess" in msg
        popMsg.closeMsg().click()

    def test_searchproduct(self):
        log = self.getLogger()
        search = SearchPage(self.driver)
        keyword = search.searchKeyword
        log.info("Search Keyword : " + keyword)
        search.enterSearchProduct().send_keys(keyword)
        search.clickSearchButton().click()
        self.driver.refresh()
        time.sleep(2)

    def test_addProductToCart(self):
        addtocartobj = CartPage(self.driver)
        productgrid = addtocartobj.getProductsGrid()
        addbutton = addtocartobj.clickAddToCart()
        for product in productgrid:
            product.click()
            for add in addbutton:
                add.click()
        TestOne.test_popupmsg(self)
        addtocartobj.clickCartIcon().click()
        addtocartobj.clickCartButton().click()
        addtocartobj.clickCheckOutButton().click()

    def test_checkOutPage(self):
        checkoutobj = CheckOutPage(self.driver)
        self.driver.refresh()
        time.sleep(3)
        checkoutRadio = checkoutobj.getcheckoutRadio()
        for radiobutton in checkoutRadio:
            if radiobutton.text == "Delivery":
                radiobutton.click()

    def test_checkOutAddAddress(self):
        checkoutobj = CheckOutPage(self.driver)
        time.sleep(2)
        checkoutobj.enterAddressName().send_keys("Test")
        checkoutobj.clickPincodeDropdown().click()
        time.sleep(2)
        xpathlocatorPincode = checkoutobj.pincodeXpath
        self.verifyXpathPresence(xpathlocatorPincode)
        checkoutobj.clickOnPincode().click()
        time.sleep(2)
        checkoutobj.clickAreaDropdown().click()
        xpathlocatorArea = checkoutobj.areaXpath
        self.verifyXpathPresence(xpathlocatorArea)
        checkoutobj.clickOnArea().click()
        time.sleep(2)
        checkoutobj.enterAddress().send_keys("9th Main Rd, HBR Layout 4th Block")
        checkoutobj.enterLandMark().send_keys("FAITH AG PRAYER FELLOWSHIP")
        checkoutobj.enterMobileNumber().send_keys("8971393466")
        checkoutobj.clickSubmitAddress().click()
        TestOne.test_popupmsg(self)

    def test_timeSlot(self):
        checkoutobj = CheckOutPage(self.driver)
        checkoutobj.clickDatePicker().click()
        csslocatorDate = checkoutobj.csspickdate
        self.verifyCssPresence(csslocatorDate)
        checkoutobj.clickPickDateCssButton().click()
        checkoutobj.clickSelectDate().click()
        scrollPath = checkoutobj.scrollPageXpath
        self.verifyXpathPresence(scrollPath)
        checkoutobj.clickScrollXpathButton().click()
        self.scrollDown(scrollPath)
        time.sleep(2)
        checkoutobj.selectTimeSlot().click()

    def test_paymentMethods(self):
        checkoutobj = CheckOutPage(self.driver)
        checkoutRadio = checkoutobj.getcheckoutRadio()
        for radiobutton in checkoutRadio:
            if radiobutton.text == "Cash on Delivery":
                radiobutton.click()

        time.sleep(2)

    def test_proceed(self):
        proceedObj = PlaceOrderPage(self.driver)
        proceedObj.clickPlaceOrder().click()
        TestOne.test_popupmsg(self)

    def test_viewOrder(self):
        log = self.getLogger()
        vieworderobj = OrdersPage(self.driver)
        vieworderobj.clickViewOrder().click()
        log.info(vieworderobj.getOrderNumber().text)
        orderproductname = vieworderobj.getProductName().text
        log.info(orderproductname)
        search = SearchPage(self.driver)
        keyword = search.searchKeyword
        assert keyword in orderproductname

    def test_cancelOrder(self):
        cancelorderobj = CancelOrder(self.driver)
        cancelorderobj.clickCancelOrder().click()
        TestOne.test_popupmsg(self)
        cancelorderobj.closeCancelPopup().click()

    def test_home(self):
        homeobj = HomePage(self.driver)
        homeobj.clickHome()
        time.sleep(2)
        homeobj.clickHome()

    def test_myAccount(self):
        myacc = MyAccountPage(self.driver)
        myacc.viewMyAccount().click()

    def test_deleteDefaultAddress(self):
        accdeleteAddress = MyAddressPage(self.driver)
        scrollMyAccXpath = MyAddressPage.scrollAccXpath
        self.verifyXpathPresence(scrollMyAccXpath)
        accdeleteAddress.viewMyAccount().click()
        self.scrollDown(scrollMyAccXpath)
        accdeleteAddress.clickMyAddress().click()
        time.sleep(2)
        accdeleteAddress.getAddressGrid().click()
        time.sleep(2)
        accdeleteAddress.clickMyAddressDelete().click()
        time.sleep(2)
        accdeleteAddress.clickMyAddressDeletePopup().click()
        TestOne.test_popupmsg(self)

    def test_addMyAccAddress(self):
        accAddAddress = MyAddressPage(self.driver)
        TestOne.test_myAccount(self)
        time.sleep(2)
        scrollMyAccXpath = MyAddressPage.scrollAccXpath
        self.verifyXpathPresence(scrollMyAccXpath)
        accAddAddress.viewMyAccount().click()
        self.scrollDownArrow(scrollMyAccXpath)
        accAddAddress.clickMyAddress().click()
        accAddAddress.clickAddEditAddressTab().click()
        accAddAddress.enterAddressName().send_keys("Test")
        pincodeXpath = accAddAddress.pincodeXpath
        accAddAddress.selectPincodeDropdown().click()
        self.verifyXpathPresence(pincodeXpath)
        accAddAddress.selectPincodeValue().click()
        areaXpath = accAddAddress.areaXpath
        accAddAddress.selectAreaDropDown().click()
        self.verifyXpathPresence(areaXpath)
        accAddAddress.selectAreaValue().click()
        accAddAddress.enterFullAddress().send_keys("9th Main Rd, HBR Layout 4th Block")
        accAddAddress.enterLandmark().send_keys("FAITH AG PRAYER FELLOWSHIP")
        accAddAddress.enterMobileNumber().send_keys("8971393466")
        accAddAddress.submitAddress().click()
        TestOne.test_popupmsg(self)

    def test_editMyAccAddress(self):
        accEditAddress = MyAddressPage(self.driver)
        TestOne.test_myAccount(self)
        time.sleep(2)
        scrollMyAccXpath = MyAddressPage.scrollAccXpath
        self.verifyXpathPresence(scrollMyAccXpath)
        accEditAddress.viewMyAccount().click()
        self.scrollDownArrow(scrollMyAccXpath)
        accEditAddress.clickMyAddress().click()
        time.sleep(2)
        accEditAddress.getAddressGrid().click()
        time.sleep(2)
        accEditAddress.editMyAddress().click()
        time.sleep(1)
        accEditAddress.enterMobileNumber().clear()
        time.sleep(1)
        accEditAddress.enterMobileNumber().send_keys("9901449102")
        accEditAddress.enterMobileNumber().send_keys(Keys.TAB)
        scrollMyAccXpath = accEditAddress.editScrollXpath
        self.scrollOnceDownArrow(scrollMyAccXpath)
        time.sleep(2)
        accEditAddress.updateAddress().click()
        TestOne.test_popupmsg(self)
        time.sleep(2)
        TestOne.test_deleteDefaultAddress(self)

    def test_validateWallet(self):
        log = self.getLogger()
        walletObj = WalletPage(self.driver)
        TestOne.test_myAccount(self)
        walletObj.viewMyAccount().click()
        time.sleep(1)
        dashboardValues = walletObj.getWalletAmount()
        walletlist = []
        NoWallet = "₹0.00"
        for values in dashboardValues:
            walletlist.append(values.text)

        log.info("Wallet first item :" + walletlist[0])
        if walletlist[0] == NoWallet:
            log.info("Wallet Amount Not Available for this User ")
        else:
            walletObj.viewWalletDetails().click()
            log.info("This user have some wallet")
            time.sleep(2)
            walletDetails = walletObj.getWalletDetails()
            for wdetails in walletDetails:
                walletDetails = wdetails.text
                print("Wallet Details : " + walletDetails)
            time.sleep(1)

            # Promo Cashback
            promoCashbackValues = walletObj.getPromoCashbackValues()
            log.info("Promo Cashback Details")
            for promo in promoCashbackValues:
                promocashdetails = promo.text
                log.info("Promo Cashback Details" + promocashdetails)
            time.sleep(1)

            # Referral Cashback
            walletObj.viewReferralCashback().click()
            log.info("Referral Cashback Details")
            referralCashbackDetails = walletObj.getReferralCashback()
            log.info("Referral Cashback Details : " + referralCashbackDetails)
            time.sleep(1)

            # Redeem Cashback
            walletObj.viewRedeemCashback().click()
            redeemCashbackValues = walletObj.getRedeemCashbackDetails()
            log.info("Redeemed Cashback Details")
            for redeem in redeemCashbackValues:
                redeemValues = redeem.text
                log.info("Redeem details :" + redeemValues)

    def test_myOrders(self):
        log = self.getLogger()
        myOrdersObj = MyOrdersPage(self.driver)
        TestOne.test_myAccount(self)
        myOrdersObj.viewMyAccount().click()
        time.sleep(2)
        ordersCountList = []
        orderCounts = myOrdersObj.getOrdersCount()
        for count in orderCounts:
            ordersCountList.append(count.text)

        log.info("Offline Orders :" + ordersCountList[0])
        log.info("Online Orders :" + ordersCountList[1])
        log.info("Reorder Orders :" + ordersCountList[2])
        time.sleep(2)

    def test_myOrdersOffline(self):
        myOrdersObj = MyOrdersPage(self.driver)
        # View Orders
        myOrdersObj.viewOrders().click()
        time.sleep(2)
        # Offline Orders
        myOrdersObj.viewOfflineOrders().click()
        time.sleep(2)
        offlineOrdersList = []
        offlineOrders = myOrdersObj.getOfflineOrdersList()
        for offline in offlineOrders:
            offlineOrdersList.append(offline.text)

        print(offlineOrdersList)

    def test_myOrdersOnline(self):
        log = self.getLogger()
        myOrdersObj = MyOrdersPage(self.driver)
        # Online Orders
        onlineOrdersList = []
        myOrdersObj.viewOnlineOrders().click()
        time.sleep(2)
        # Handling table
        # get number of rows
        noOfRows = len(myOrdersObj.getNoOfRows()) + 1
        time.sleep(1)
        # get number of columns
        noOfColumns = len(myOrdersObj.getNoOfColumns()) - 1
        # iterate over the rows, to ignore the headers we have started the i with '1
        for i in range(1, noOfRows):
            # reset the row data every time
            ro = []
            # iterate over columns
            for j in range(1, noOfColumns):
                # get text from the i th row and j th column
                ro.append(self.driver.find_element_by_xpath(
                    "//table[starts-with(@class, 'table')]/tbody/tr[" + str(i) + "]/td[" + str(j) + "]").text)
            # add the row data to allData of the self.table
            onlineOrdersList.append(ro)
        print(onlineOrdersList[0])
        time.sleep(2)
        viewOrder = myOrdersObj.viewOnlineOrder()
        for view in viewOrder:
            view.click()
            break
        time.sleep(1)
        OrderNumber = myOrdersObj.getOrderNumber().text
        print(OrderNumber)
        orderProductName = myOrdersObj.getOrderProductName().text
        print(orderProductName)
        orderProductQty = myOrdersObj.getOrderProductQty().text
        print(orderProductQty)
        orderTotal = myOrdersObj.getOrderTotal().text
        print(orderTotal)
        myOrdersObj.closeOrderPopup().click()
        myOrdersObj.clickOnHome().click()

    def test_myWishList(self):
        mylistobj = MyWishListPage(self.driver)
        self.driver.refresh()
        time.sleep(2)
        mylistobj.clickOnWishList().click()
        AutomaticListCount = mylistobj.getAutoListCount()
        print(AutomaticListCount)
        ManualListCount = mylistobj.getManualListCount()
        print(ManualListCount)

    def test_myAutomaticDailyList(self):
        myautodailylistobj = AutomaticListPage(self.driver)
        myautodailylistobj.viewAutoListPage().click()
        time.sleep(2)
        myautodailylistobj.createNewAutoList().click()
        myautodailylistobj.enterAutoDialylistName().send_keys("My Daily List")
        myautodailylistobj.clickOnScheduleTypeDropDown().click()
        time.sleep(1)
        myautodailylistobj.selectScheduleTypeDialy().click()
        time.sleep(1)
        myautodailylistobj.clickOnScheduleHoursDropDown().click()
        time.sleep(1)
        myautodailylistobj.selectScheduleHours().click()
        time.sleep(1)
        myautodailylistobj.clickOnCreateAutoList().click()
        TestOne.test_popupmsg(self)

    def test_deleteAutoList(self):
        deleteAutolistobj = DeleteAutoList(self.driver)
        time.sleep(2)
        deleteAutolistobj.clickOnDeleteListIcon().click()
        time.sleep(1)
        deleteAutolistobj.clickOnDeleteListPopup().click()
        time.sleep(2)

    def test_myAutomaticWeeklyList(self):
        myautoweeklylistobj = AutomaticListPage(self.driver)
        myautoweeklylistobj.createNewAutoList().click()
        myautoweeklylistobj.enterAutoWeeklylistName().send_keys("My Weekly List")
        myautoweeklylistobj.clickOnScheduleTypeDropDown().click()
        time.sleep(1)
        myautoweeklylistobj.selectScheduleTypeWeekly().click()
        time.sleep(2)
        myautoweeklylistobj.clickOnScheduleWeekDropDown().click()
        time.sleep(2)
        myautoweeklylistobj.selectScheduleWeek().click()
        time.sleep(1)
        myautoweeklylistobj.clickOnScheduleHoursDropDown().click()
        time.sleep(2)
        myautoweeklylistobj.selectScheduleHours().click()
        time.sleep(2)
        myautoweeklylistobj.clickOnCreateAutoList().click()
        time.sleep(1)
        TestOne.test_popupmsg(self)
        TestOne.test_deleteAutoList(self)

    def test_myAutomaticMonthlyList(self):
        myautomonthlylistobj = AutomaticListPage(self.driver)
        myautomonthlylistobj.createNewAutoList().click()
        myautomonthlylistobj.enterAutoMonthlylistName().send_keys("My Monthly List")
        myautomonthlylistobj.clickOnScheduleTypeDropDown().click()
        time.sleep(1)
        myautomonthlylistobj.selectScheduleTypeMonthly().click()
        time.sleep(2)
        myautomonthlylistobj.clickOnScheduleDateDropdown().click()
        time.sleep(2)
        myautomonthlylistobj.selectScheduleDate().click()
        time.sleep(1)
        myautomonthlylistobj.clickOnScheduleHoursDropDown().click()
        time.sleep(2)
        myautomonthlylistobj.selectScheduleHours().click()
        time.sleep(1)
        myautomonthlylistobj.clickOnCreateAutoList().click()
        time.sleep(1)
        TestOne.test_popupmsg(self)
        TestOne.test_deleteAutoList(self)

    def test_addProductToList(self):
        homeobj = HomePage(self.driver)
        homeobj.clickHome()
        # search product (TestOne.test_searchProduct(self)
        log = self.getLogger()
        search = SearchPage(self.driver)
        keyword = search.searchKeyword
        search.enterSearchProduct().send_keys(keyword)
        search.clickSearchButton().click()
        self.driver.refresh()
        time.sleep(2)
        # Add product to list
        addproductlistobj = AddProductList(self.driver)
        productgrid = addproductlistobj.getProductsGrid()
        print(len(productgrid))
        addtolistbutton = addproductlistobj.getAddToListButton()
        print(len(addtolistbutton))
        for product in productgrid:
            product.click()
            time.sleep(1)
            for add in addtolistbutton:
                add.click()
                time.sleep(1)

        TestOne.test_popupmsg(self)
        homeobj.clickHome()
        self.driver.refresh()

    def test_viewManualListProduct(self):
        log = self.getLogger()
        viewmanuallistproducts = ViewManualListProduct(self.driver)
        viewmanuallistproducts.clickOnMyWishList()
        time.sleep(1)
        manualListcount = viewmanuallistproducts.getManualLIstCount()
        print(manualListcount)
        manuallistDetails = []
        baseTableXpath = viewmanuallistproducts.baseXpath
        if int(manualListcount) >= 1:
            log.info("Default List Available")
            viewmanuallistproducts.viewManualList()
            time.sleep(1)
            # Handling table
            # get number of rows
            noOfRows = len(self.driver.find_elements_by_xpath(baseTableXpath + "/tr/td[1]")) + 1
            print(noOfRows)
            time.sleep(1)
            # get number of columns
            noOfColumns = len(self.driver.find_elements_by_xpath(baseTableXpath + "/tr[1]/td")) - 3
            print(noOfColumns)
            # iterate over the rows, to ignore the headers we have started the i with '1
            for i in range(1, noOfRows):
                # reset the row data every time
                ro = []
                # iterate over columns
                for j in range(1, noOfColumns):
                    # get text from the i th row and j th column
                    ro.append(self.driver.find_element_by_xpath(baseTableXpath + "/tr[" + str(i) + "]/td[" + str(j) + "]").text)

                # add the row data to allData of the self.table
                manuallistDetails.append(ro)

            print(manuallistDetails[0])
            time.sleep(1)

    def test_manualListPlaceOrder(self):
        manuallistplaceorderobj = ManualListPlaceOrder(self.driver)
        manuallistplaceorderobj.viewManualListDetails()
        time.sleep(1)
        manuallistplaceorderobj.clickToProcced()
        time.sleep(1)
        manuallistplaceorderobj.selectPaymentTypes()
        time.sleep(1)
        manuallistplaceorderobj.clickOnPlaceOrder()
        TestOne.test_popupmsg(self)
        time.sleep(2)
        manuallistplaceorderobj.clickViewOrder()
        print(manuallistplaceorderobj.getOrderNumber())
        print(manuallistplaceorderobj.getproductName())
        manuallistplaceorderobj.clickOnCancelOrder()
        time.sleep(2)
        TestOne.test_popupmsg(self)
        manuallistplaceorderobj.clickOnPopupClose()

    def test_deleteManualList(self):
        log = self.getLogger()
        homeobj = HomePage(self.driver)
        time.sleep(2)
        homeobj.clickHome()
        viewmanuallistproducts = ViewManualListProduct(self.driver)
        viewmanuallistproducts.clickOnMyWishList()
        viewmanuallistproducts.viewManualList()
        time.sleep(2)
        deletemanuallist = DeleteManualList(self.driver)
        deletemanuallist.clickOnDeleteSingleManuallist()
        deletemanuallist.clickOnPopupOk()
        listnotemptymsg = deletemanuallist.getErrorMsg()
        log.info(listnotemptymsg)
        deletemanuallist.closePopMsg()
        if listnotemptymsg == "List is not empty. Please move or delete the products":
            deletemanuallist.viewManualList()
            time.sleep(1)
            print(deletemanuallist.getProductName())
            deletemanuallist.deleteProductFromList()
            TestOne.test_popupmsg(self)
            time.sleep(1)
            deletemanuallist.backToManualList()
            time.sleep(1)
            deletemanuallist.clickOnDeleteSingleManuallist()
            deletemanuallist.clickOnPopupOk()
            time.sleep(1)
            log.info("List deleted successfully")
        else:
            deletemanuallist.clickOnDeleteSingleManuallist()
            deletemanuallist.clickOnPopupOk()
            log.info("List deleted successfully")
            
        
    def test_addMultipleProductsToList(self):
        addmultipleproducts = AddMultipleProductToList(self.driver)
        addmultipleproducts.enterSearchkeyword()
        addmultipleproducts.clickToSearchProduct()
        self.driver.refresh()
        productgrid = addmultipleproducts.getProductGrids()
        addtolist = addmultipleproducts.getAddToListButtons()
        searchProductGrids = len(addmultipleproducts.getSearchProductGridLength()) +1
        time.sleep(1)
        for i in range(1, searchProductGrids):
            i = i - 1
            productgrid[i].click()
            time.sleep(2)
            addtolist[i].click()
            time.sleep(1)
            TestOne.test_popupmsg(self)

    def test_createDailyListToMoveProducts(self):
        myautodailylistobj = AutomaticListPage(self.driver)
        myautodailylistobj.clickOnWishListMenuIcon().click()
        myautodailylistobj.viewAutoListPage().click()
        time.sleep(2)
        myautodailylistobj.createNewAutoList().click()
        myautodailylistobj.enterAutoDialylistName().send_keys("My Daily List")
        myautodailylistobj.clickOnScheduleTypeDropDown().click()
        time.sleep(1)
        myautodailylistobj.selectScheduleTypeDialy().click()
        time.sleep(1)
        myautodailylistobj.clickOnScheduleHoursDropDown().click()
        time.sleep(1)
        myautodailylistobj.selectScheduleHours().click()
        time.sleep(1)
        myautodailylistobj.clickOnCreateAutoList().click()
        TestOne.test_popupmsg(self)

    def test_moveProductsToList(self):
        log = self.getLogger()
        moveproductsTolist = MoveProductsToList(self.driver)
        moveproductsTolist.clickToViewWishList()
        manualListcount = moveproductsTolist.getManualListCount()
        if manualListcount >= "1":
            log.info("Default List Available")
            moveproductsTolist.clickToViewManualList()
            time.sleep(1)
        else:
            log.info("No List Available, Please Create Manual List")

        moveproductsTolist.clickToViewManualListProducts()
        time.sleep(2)
        productsCheckBoxs = moveproductsTolist.clickOnCheckBox()
        for checkBox in productsCheckBoxs:
            checkBox.click()
            break
        time.sleep(1)
        moveproductsTolist.clickToMoveToList()
        time.sleep(1)
        moveproductsTolist.clickToSelectAutoList()
        time.sleep(1)
        moveproductsTolist.selectAutoList()
        time.sleep(1)
        moveproductsTolist.clickToSelectDailyList()
        TestOne.test_popupmsg(self)

    def test_autoListPlaceOrder(self):
        log = self.getLogger()
        autolistplaceorder = AutoListPlaceOrder(self.driver)
        autolistplaceorder.clickToViewWishList()
        autolistcount = autolistplaceorder.getAutoListCount()
        if autolistcount >= "1":
            log.info("Auto List Available")
            autolistplaceorder.clickToViewAutoList()
            autolistplaceorder.clickToViewAutoListProducts()
            time.sleep(1)
            autolistplaceorder.clickToProcced()
            time.sleep(1)
            autolistplaceorder.selectPaymentTypes()
            time.sleep(1)
            autolistplaceorder.clickOnPlaceOrder()
            TestOne.test_popupmsg(self)
            time.sleep(2)
            autolistplaceorder.clickViewOrder()
            print(autolistplaceorder.getOrderNumber())
            print(autolistplaceorder.getproductName())
            autolistplaceorder.clickOnCancelOrder()
            time.sleep(2)
            TestOne.test_popupmsg(self)
            autolistplaceorder.clickOnPopupClose()
        else:
            log.info("No List Available, Please Create Manual List")

    def test_deleteAutoListWithProduct(self):
        log = self.getLogger()
        deleteautolist = DeteleAutoListWithProduct(self.driver)
        deleteautolist.clickToViewWishList()
        autolistcount = deleteautolist.getAutoListCount()
        if autolistcount >= "1":
            log.info('Auto list Available')
            deleteautolist.clickToViewAutoList()
            deleteautolist.clickOnDelete()
            deleteautolist.clickOnPopupOk()
            listnotemptymsg = deleteautolist.getErrorMsg()
            log.info(listnotemptymsg)
            deleteautolist.closePopMsg()
            if listnotemptymsg == "List is not empty. Please move or delete the products":
                deleteautolist.viewAutoListProducts()
                time.sleep(1)
                deleteproducts = deleteautolist.getDeleteProductButton()
                deletebuttoncount = len(deleteautolist.getDeleteProductButton()) +1
                print(deletebuttoncount)
                for i in range(1, deletebuttoncount):
                    i = 1
                    self.driver.find_element_by_xpath("//table[starts-with(@class,'table')]/tbody/tr["+str(i)+"]/td[8]").click()
                    time.sleep(1)
                    TestOne.test_popupmsg(self)
                    self.driver.refresh()

                deleteautolist.getBackToAutoList()
                deleteautolist.clickOnDelete()
                deleteautolist.clickOnPopupOk()
            else:
                deleteautolist.clickOnDelete()
                deleteautolist.clickOnPopupOk()
                log.info("List deleted successfully")

    def test_deleteManualListAfterProductMove(self):
        log = self.getLogger()
        viewmanuallistproducts = ViewManualListProduct(self.driver)
        viewmanuallistproducts.clickOnMyWishList()
        viewmanuallistproducts.viewManualList()
        time.sleep(2)
        deletemanuallist = DeleteManualList(self.driver)
        deletemanuallist.clickOnDeleteSingleManuallist()
        deletemanuallist.clickOnPopupOk()
        log.info("List deleted successfully")

    @pytest.fixture(params=LoginData.getTestData("Credential1"))
    def getData(self, request):
        return request.param

var oMain = oMain ? oMain : {};

oMain.Constants = {
    PREVIOUS: "prev",
    NEXT: "next"
}

oMain.Head = null;
oMain.Prev = null;
oMain.Current = null;

oMain.List = function(oElement) {
    this.oElement = oElement;
    this.next = null;
    this.prev = null;
};

oMain.onLoad = function() {
    let oFormGroup = document.getElementsByClassName("form-group");
    let oHead = new oMain.List(oFormGroup[0]);
    oMain.Head = oHead;
    oMain.Current = oHead;
    let oCurrent = oHead;
    let oPrev = oHead;
    for(let i = 1; i < oFormGroup.length; i++) {
        oFormGroup[i].style.display = "none";
        let temp = new oMain.List(oFormGroup[i]);
        oCurrent.next = temp;
        oCurrent.prev = oPrev;
        oPrev = oCurrent;
        oCurrent = oCurrent.next;
    }
};

oMain.handleButtonAction = function(sAction) {
    if (sAction.toLowerCase() === oMain.Constants.PREVIOUS.toLowerCase()) {
        if (null != oMain.Current) {
            oMain.Current.prev.oElement.style.display = "";
            oMain.Current.oElement.style.display = "none";
            oMain.Current = oMain.Current.prev;
        }
        if (oMain.Head == oMain.Current) {
            document.getElementsByClassName("prev")[0].style.display = "none";
        }
    }
    if (sAction.toLowerCase() === oMain.Constants.NEXT.toLowerCase()) {
        if (null != oMain.Current.next && null != oMain.Current.next.next) {
            document.getElementsByClassName("prev")[0].style.display = "";
            oMain.Current.next.oElement.style.display = "";
            oMain.Current.oElement.style.display = "none";
            if ("submit" == oMain.Current.next.next.oElement.childNodes[1].name) {
                document.getElementsByClassName("next")[0].style.display = "none";
                document.getElementsByClassName("prev")[0].style.display = "none";
                document.getElementsByName("submit")[0].parentElement.style.display = "";
            }
            oMain.Current = oMain.Current.next;
        }
    }
};

$(document).ready(function() {
    oMain.onLoad();
    let prev = document.getElementsByClassName("prev")[0];
    let next = document.getElementsByClassName("next")[0];
    prev.style.display = "none";
    prev.addEventListener("click", function() {
        oMain.handleButtonAction(oMain.Constants.PREVIOUS);
    });
    next.addEventListener("click", function() {
        oMain.handleButtonAction(oMain.Constants.NEXT);
    });
});
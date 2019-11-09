<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Index.aspx.cs" Inherits="IndexPage1.Index" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            text-align: center;
        }
        .auto-style2 {
            text-align: left;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Label ID="Label1" runat="server" Font-Bold="True" Font-Size="XX-Large" Text="Directory Page"></asp:Label>
            <br />
            <hr />
            <div class="auto-style1">
                <div class="auto-style1">
                    <br />
                    Filter by Document Type: <asp:DropDownList ID="DropDownList1" runat="server" AutoPostBack="True" DataSourceID="SqlDataSource2" DataTextField="DocType" DataValueField="DocType" AppendDataBoundItems="true" OnSelectedIndexChanged="DropDownList1_SelectedIndexChanged"> <asp:ListItem Text="All Documents" Value="" />
                    </asp:DropDownList>
                    <asp:SqlDataSource ID="SqlDataSource2" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" SelectCommand="SELECT DISTINCT [DocType] FROM [Table]"></asp:SqlDataSource>
                    <br />
                    <br />
                </div>
                <div class="auto-style2">
                    <asp:GridView ID="GridView1" runat="server" AllowPaging="True" AllowSorting="True" AutoGenerateColumns="False" DataSourceID="SqlDataSource1" Height="200px" HorizontalAlign="Center" OnSelectedIndexChanged="GridView1_SelectedIndexChanged" PageSize="5" Width="699px" DataKeyNames="Id">
                        <Columns>
                            <asp:BoundField DataField="DocTitle" HeaderText="DocTitle" SortExpression="DocTitle" >
                            </asp:BoundField>
                            <asp:BoundField DataField="DocType" HeaderText="DocType" SortExpression="DocType">
                            </asp:BoundField>
                            <asp:BoundField DataField="UploadDate" HeaderText="UploadDate" SortExpression="UploadDate" >
                            </asp:BoundField>
                            <asp:BoundField DataField="DocLink" HeaderText="DocLink" SortExpression="DocLink"></asp:BoundField>
                        </Columns>
                    </asp:GridView>
                    <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" SelectCommand="SELECT * FROM [Table]" FilterExpression="DocType='{0}'"> <FilterParameters> <asp:ControlParameter Name="DocType" ControlID="DropDownList1" PropertyName="SelectedValue" /></FilterParameters></asp:SqlDataSource>
                </div>
            </div>
        </div>
    </form>
</body>
</html>

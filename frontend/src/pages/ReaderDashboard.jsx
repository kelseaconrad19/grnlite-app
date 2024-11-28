import React, { useState } from 'react';
import styled from 'styled-components';
import Switch from 'react-switch';
import { Form, Button, FormGroup } from 'react-bootstrap';



// Styled Components
const DashboardContainer = styled.div`
  display: flex;
  height: 100vh;
  background-color: #f4f4f4;
  overflow-x: hidden;
`;

const Sidebar = styled.div`
  width: 250px;
  background-color: #145a32;
  color: white;
  display: flex;
  flex-direction: column;
  padding: 20px;
  transition: all 0.3s ease;
  overflow-y: auto;

  &:hover {
    background-color: #1f8341;
  }
`;

const SidebarItem = styled.div`
  padding: 15px 10px;
  margin: 5px 0;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s ease, transform 0.2s ease;
  display: flex;
  align-items: center;

  &:hover {
    background-color: #27ae60;
    transform: scale(1.05);
  }

  &.active {
    background-color: #2ecc71;
  }

  svg {
    margin-right: 10px;
  }
`;

const Topbar = styled.div`
  width: 100%;
  height: 60px;
  background-color: white;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
`;

const Content = styled.div`
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  max-width: 100%;
  box-sizing: border-box;
`;

const DashboardTitle = styled.h1`
  color: #145a32;
  font-family: 'Courier New', Courier, monospace;
`;

const Card = styled.div`
  padding: 15px;
  background-color: white;
  margin-bottom: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
`;

const ClickButton = styled.button`

  padding: 10px 20px;
  background-color: #27ae60;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;

  &:hover {
    background-color: #2ecc71;
  }
`;

const Input = styled.input`
  padding: 10px;
  margin-top: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  width: 100%;
`;

const Textarea = styled.textarea`
  padding: 10px;
  margin-top: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  width: 100%;
  resize: none;
`;

const ToggleContainer = styled.div`
  margin-top: 15px;

  label {
    font-weight: bold;
    display: block;
    margin-bottom: 5px;
  }

  input {
    margin-right: 10px;
  }
`;

const NotificationBell = styled.div`
  cursor: pointer;
  font-size: 1.5rem;
  color: #145a32;
  position: relative;

  &:hover {
    color: #27ae60;
  }

  span {
    position: absolute;
    top: -5px;
    right: -10px;
    background-color: red;
    color: white;
    border-radius: 50%;
    padding: 5px 8px;
    font-size: 0.9rem;
  }
`;

const Icon = styled.i`
  font-size: 1.2rem;
  margin-right: 8px;
`;

const ButtonRow = styled.div`
  display: flex;
  justify-content: flex-start;
  gap: 20px;
  margin-bottom: 20px;
`;

const ProfilePicContainer = styled.div`
  margin-bottom: 20px;
`;

const ProfilePicLabel = styled.label`
  display: block;
  margin-bottom: 10px;
  font-weight: bold;
`;

const ProfilePicInput = styled.input`
  display: none;
`;

const ProfilePicButton = styled.label`
  cursor: pointer;
  background-color: #27ae60;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  display: inline-block;

  &:hover {
    background-color: #2ecc71;
  }
`;

const FormGroup2 = styled.div`
  margin-bottom: 20px;
`;

const GroupContainer = styled.div`
  margin-bottom: 20px;
`;

const GroupList = styled.div`
  list-style-type: none;
  padding: 0;
`;

const GroupItem = styled.div`
  background-color: #e9f7ef;
  border-radius: 5px;
  margin: 10px 0;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;

  &:hover {
    background-color: #d5f5e3;
  }
`;

// Main Component
const ReaderDashboard = () => {
  const [activeTab, setActiveTab] = useState('myBooks');
  const [notifications, setNotifications] = useState(5);
  const [groups, setGroups] = useState([
    { id: 1, name: 'Fantasy Readers', description: 'Explore fantasy worlds together.' },
    { id: 2, name: 'Beta Reviewers', description: 'Support authors with feedback.' },
  ]);
  const [resources, setResources] = useState([
    { id: 1, name: 'Free E-Book Libraries', description: 'Discover free e-books across genres.' },
    { id: 2, name: 'Writing Workshops', description: 'Learn and improve with top authors.' },
  ]);
  const [newGroup, setNewGroup] = useState({ name: '', description: '' });
  const [newResource, setNewResource] = useState({ name: '', description: '' });
  const [profilePic, setProfilePic] = useState(null);
  const [settings, setSettings] = useState({
    contactPhone: '',
  });

  const handleNotificationClick = () => {
    alert(`You have ${notifications} new notifications`);
    setNotifications(0);
  };

  const handleCreateGroup = () => {
    if (newGroup.name && newGroup.description) {
      setGroups([...groups, { id: groups.length + 1, ...newGroup }]);
      setNewGroup({ name: '', description: '' });
    }
  };

  const handleAddResource = () => {
    if (newResource.name && newResource.description) {
      setResources([...resources, { id: resources.length + 1, ...newResource }]);
      setNewResource({ name: '', description: '' });
    }
  };

  const handleSignOut = () => {
    alert('You have been signed out.');
    localStorage.removeItem('user');
    window.location.href = '/'; // Redirect to homepage
  };

  const handleProfilePicChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setProfilePic(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleContactChange = (e) => {
    setSettings({ ...settings, contactPhone: e.target.value });
  };
  const [feedback, setFeedback] = useState({
    manuscriptId: '',
    plot: '',
    characters: '',
    pace: '',
  });
  
  const [profile, setProfile] = useState({
    bio: '',
    portfolio: '',
    payRate: '',
    ratings: [], // Optional
  });
  const [profileExists, setProfileExists] = useState(false); // Tracks if the profile is already created

  const handleSubmitProfile = () => {
    // API call to save the profile
    setProfileExists(true);
  };
  

  const renderContent = () => {
    switch (activeTab) {
      case 'myBooks':
        return (
          <>
            <DashboardTitle>My Books</DashboardTitle>
            <ButtonRow>
              <Button>Add to Favorites</Button>
              <Button>Mark as Read</Button>
            </ButtonRow>
            <Card>
              <h3>Book Title 1</h3>
              <p>Progress: Chapter 10 of 30</p>
            </Card>
            <Card>
              <h3>Book Title 2</h3>
              <p>Progress: Chapter 5 of 15</p>
            </Card>
          </>
        );
        case 'profile':
          return (
            <>
              <DashboardTitle>Profile Settings</DashboardTitle>
        
              {/* Name Input */}
              <FormGroup>
                <label htmlFor="name">Full Name:</label>
                <Input
                  type="text"
                  id="name"
                  placeholder="Enter your full name"
                  value={settings.name || ''}
                  onChange={(e) => setSettings({ ...settings, name: e.target.value })}
                />
              </FormGroup>
        
            {/* Profile Picture */}
            <FormGroup>
              <label htmlFor="profilepic-upload">Upload Profile Pic:</label>
              <Input type="file" id="profilepic-upload" />
            </FormGroup>
                
               
              {/* Bio Input */}
              <FormGroup>
                <label htmlFor="bio">Bio:</label>
                <Textarea
                  id="bio"
                  placeholder="Write a short bio here..."
                  value={settings.bio || ''}
                  onChange={(e) => setSettings({ ...settings, bio: e.target.value })}
                />
              </FormGroup>
        
              {/* Phone Number Input */}
              <FormGroup>
                <label htmlFor="phone-number">Phone Number:</label>
                <Input
                  type="tel"
                  id="phone-number"
                  placeholder="Enter your phone number"
                  name="contactPhone"
                  value={settings.contactPhone || ''}
                  onChange={handleContactChange}
                />
              </FormGroup>
        
              {/* Email Input */}
              <FormGroup>
                <label htmlFor="email">Email Address:</label>
                <Input
                  type="email"
                  id="email"
                  placeholder="Enter your email address"
                  value={settings.email || ''}
                  onChange={(e) => setSettings({ ...settings, email: e.target.value })}
                />
              </FormGroup>
        
              {/* Location Input */}
              <FormGroup>
                <label htmlFor="location">Location:</label>
                <Input
                  type="text"
                  id="location"
                  placeholder="Enter your location"
                  value={settings.location || ''}
                  onChange={(e) => setSettings({ ...settings, location: e.target.value })}
                />
              </FormGroup>
        
              {/* Save Button */}
              <Button onClick={() => alert('Profile updated!')}>
                Save Changes
              </Button>
            </>
          ); 
          
case 'betaReaderProfile':
  return (
    <>
      <DashboardTitle>Beta Reader Profile</DashboardTitle>
      {!profileExists ? (
        // Profile Setup Form
        <Form>
          <FormGroup>
            <label htmlFor="bio">Brief Bio:</label>
            <textarea
              id="bio"
              name="bio"
              value={profile.bio}
              onChange={(e) =>
                setProfile({ ...profile, [e.target.name]: e.target.value })
              }
              placeholder="Write a short bio to highlight your skills and experience"
            />
          </FormGroup>

          <FormGroup>
            <label htmlFor="portfolio">Portfolio Examples:</label>
            <textarea
              id="portfolio"
              name="portfolio"
              value={profile.portfolio}
              onChange={(e) =>
                setProfile({ ...profile, [e.target.name]: e.target.value })
              }
              placeholder="Describe examples of feedback you've given (redact titles/identifiers)"
            />
          </FormGroup>

          <FormGroup>
            <label htmlFor="payRate">Desired Pay Rate:</label>
            <Input
              type="number"
              id="payRate"
              name="payRate"
              value={profile.payRate}
              onChange={(e) =>
                setProfile({ ...profile, [e.target.name]: e.target.value })
              }
              placeholder="Enter your pay rate (e.g., $10/hour)"
            />
          </FormGroup>

          <Button onClick={handleSubmitProfile}>Save Profile</Button>
        </Form>
      ) : (
        // Profile View Section
        <div>
          <h3>Your Profile</h3>
          <p>
            <strong>Bio:</strong> {profile.bio}
          </p>
          <p>
            <strong>Portfolio:</strong> {profile.portfolio}
          </p>
          <p>
            <strong>Pay Rate:</strong> ${profile.payRate}/hour
          </p>

          {/* Optional: Ratings Section */}
          {profile.ratings && (
            <>
              <h4>Ratings</h4>
              <ul>
                {profile.ratings.map((rating, index) => (
                  <li key={index}>
                    {rating.authorName}: {rating.comment} ({rating.score}/5)
                  </li>
                ))}
              </ul>
            </>
          )}

          <Button onClick={() => setProfileExists(false)}>Edit Profile</Button>
        </div>
      )}
    </>
  );


      case 'resources':
        return (
          <>
            <DashboardTitle>Resources</DashboardTitle>
            {resources.map((resource) => (
              <Card key={resource.id}>
                <h3>{resource.name}</h3>
                <p>{resource.description}</p>
                <Button>Access Resource</Button>
              </Card>
            ))}
            <Input
              placeholder="Resource Name"
              value={newResource.name}
              onChange={(e) => setNewResource({ ...newResource, name: e.target.value })}
            />
            <Textarea
              placeholder="Resource Description"
              value={newResource.description}
              onChange={(e) => setNewResource({ ...newResource, description: e.target.value })}
            />
            <Button onClick={handleAddResource}>Add Resource</Button>
          </>
        );
      case 'groups':
        return (
          <>
            <DashboardTitle>Community Groups</DashboardTitle>
            {groups.map((group) => (
              <Card key={group.id}>
                <h3>{group.name}</h3>
                <p>{group.description}</p>
                <Button>Join Group</Button>
              </Card>
            ))}
            <Input
              placeholder="Group Name"
              value={newGroup.name}
              onChange={(e) => setNewGroup({ ...newGroup, name: e.target.value })}
            />
            <Textarea
              placeholder="Group Description"
              value={newGroup.description}
              onChange={(e) => setNewGroup({ ...newGroup, description: e.target.value })}
            />
            <Button onClick={handleCreateGroup}>Create Group</Button>
          </>
        );


        
        case 'settings':
          return (
            <>
              <DashboardTitle>Account Settings</DashboardTitle>
        
              {/* Enable Dark Mode */}
              <FormGroup>
                <label htmlFor="enable-dark-mode">
                  <span>Enable Dark Mode</span>
                  <Switch
                    checked={settings.darkMode}
                    onChange={(checked) =>
                      setSettings({ ...settings, darkMode: checked })
                    }
                  />
                </label>
              </FormGroup>
        
              {/* Email Notifications */}
              <FormGroup>
                <label htmlFor="email-notifications">
                  <span>Email Notifications</span>
                  <Switch
                    checked={settings.emailNotifications}
                    onChange={(checked) =>
                      setSettings({ ...settings, emailNotifications: checked })
                    }
                  />
                </label>
              </FormGroup>
        
              {/* Profile Visibility */}
              <FormGroup>
                <label htmlFor="profile-visibility">
                  <span>Profile Visibility</span>
                  <Switch
                    checked={settings.profileVisibility}
                    onChange={(checked) =>
                      setSettings({ ...settings, profileVisibility: checked })
                    }
                  />
                </label>
              </FormGroup>
        
              {/* Contact Email */}
              <FormGroup>
                <label htmlFor="contact-email">Contact Email:</label>
                <Input
                  type="email"
                  id="contact-email"
                  name="contactEmail"
                  value={settings.contactEmail}
                  onChange={(e) =>
                    setSettings({ ...settings, contactEmail: e.target.value })
                  }
                />
              </FormGroup>
        
              {/* Contact Phone */}
              <FormGroup>
                <label htmlFor="contact-phone">Contact Phone:</label>
                <Input
                  type="text"
                  id="contact-phone"
                  name="contactPhone"
                  value={settings.contactPhone}
                  onChange={(e) =>
                    setSettings({ ...settings, contactPhone: e.target.value })
                  }
                />
              </FormGroup>
               
              {/* Social Links */}
              <FormGroup>
                <label htmlFor="social-link-facebook">Facebook:</label>
                <Input
                  type="url"
                  id="social-link-facebook"
                  name="facebookLink"
                  value={settings.facebookLink}
                  onChange={(e) =>
                    setSettings({ ...settings, facebookLink: e.target.value })
                  }
                  placeholder="Enter your Facebook URL"
                />
              </FormGroup>
              <FormGroup>
                <label htmlFor="social-link-twitter">Twitter:</label>
                <Input
                  type="url"
                  id="social-link-twitter"
                  name="twitterLink"
                  value={settings.twitterLink}
                  onChange={(e) =>
                    setSettings({ ...settings, twitterLink: e.target.value })
                  }
                  placeholder="Enter your Twitter URL"
                />
              </FormGroup>
              <FormGroup>
                <label htmlFor="social-link-linkedin">LinkedIn:</label>
                <Input
                  type="url"
                  id="social-link-linkedin"
                  name="linkedinLink"
                  value={settings.linkedinLink}
                  onChange={(e) =>
                    setSettings({ ...settings, linkedinLink: e.target.value })
                  }
                  placeholder="Enter your LinkedIn URL"
                />
              </FormGroup>
        
              {/* Change Password Button */}
              <FormGroup>
                <Button onClick={() => alert('Password change functionality coming soon!')}>
                  Change Password
                </Button>
              </FormGroup>
        
              {/* Save Settings Button */}
              <Button onClick={() => alert('Settings saved!')}>Save Settings</Button>
            </>
          );
        
        
        default:
          return <p>Unknown Tab</p>;
      }
    };

  return (
    <DashboardContainer>
      <Sidebar>
        <NotificationBell
          onClick={handleNotificationClick}
          style={{ marginLeft: '230px' }} 
        >
          🔔 {notifications > 0 && `${notifications}`}
        </NotificationBell>
        <SidebarItem onClick={() => setActiveTab('myBooks')} className={activeTab === 'myBooks' ? 'active' : ''}>
          My Books
        </SidebarItem>
        <SidebarItem onClick={() => setActiveTab('profile')} className={activeTab === 'profile' ? 'active' : ''}>
          Profile
        </SidebarItem>
        <SidebarItem onClick={() => setActiveTab('resources')} className={activeTab === 'resources' ? 'active' : ''}>
          Resources
        </SidebarItem>
        <SidebarItem onClick={() => setActiveTab('groups')} className={activeTab === 'groups' ? 'active' : ''}>
          Community Groups
        </SidebarItem>
        <SidebarItem onClick={() => setActiveTab('betaReaderProfile')} className={activeTab === 'betaReaderProfile' ? 'active' : ''}>
        Beta Reader Profile
        </SidebarItem>
        <SidebarItem onClick={() => setActiveTab('settings')} className={activeTab === 'settings' ? 'active' : ''}>
          Settings
        </SidebarItem>
        <SidebarItem onClick={handleSignOut}>
          <Icon className="fas fa-sign-out-alt" /> Sign Out
        </SidebarItem>
      </Sidebar>
      <div style={{ flex: 1, flexDirection: 'column' }}>
        <Topbar>
          <h2>Reader Dashboard</h2>
        </Topbar>
        <Content>{renderContent()}</Content>
      </div>
    </DashboardContainer>
  );
};

export default ReaderDashboard;